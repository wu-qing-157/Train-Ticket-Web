import flask, socket

import backend

from const import *
from ticket import *

app = flask.Flask(__name__)


@app.route('/')
def index():
    if 'current_user' in flask.session:
        return flask.redirect(flask.url_for('main_page'))
    else:
        return flask.redirect(flask.url_for('login'))


@app.route('/logout')
def logout():
    flask.session.pop(S_CURRENT_USER)
    flask.session.pop(S_ADMINISTRATOR)
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        user_id = flask.request.form['id']
        password = flask.request.form['password']
        try:
            result = backend.get_result("login {} {}".format(user_id, password), SZ_LOGIN, RE_LOGIN)
            if result == '1':
                flask.session[S_CURRENT_USER] = user_id
                result = backend.get_result("query_profile {}".format(flask.session[S_CURRENT_USER]),
                                            SZ_QUERY_PROFILE, RE_QUERY_PROFILE).split(' ')
                flask.session[S_CURRENT_USER] = user_id
                flask.session[S_NAME] = result[0]
                flask.session[S_EMAIL] = result[1]
                flask.session[S_PHONE] = result[2]
                flask.session[S_ADMINISTRATOR] = result[3] == '2'
                return flask.redirect(flask.url_for('main_page'))
            else:
                flask.session[S_ERR_MESSAGE] = E_PASSWORD_NOT_MATCH
        except ConnectionRefusedError:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
        except socket.timeout:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
        except SyntaxError:
            flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        flask.session[S_SET_USER_ID] = user_id
        return flask.redirect(flask.url_for('login', _method='GET'))
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            user_id = flask.session[S_SET_USER_ID]
            flask.session.pop(S_ERR_MESSAGE)
            flask.session.pop(S_SET_USER_ID)
            return flask.render_template('login.html', show_alert=True, message=message, set_id=user_id)
        else:
            return flask.render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        password = flask.request.form['password']
        name = flask.request.form['name']
        email = flask.request.form['email']
        phone = flask.request.form['phone']
        try:
            result = backend.get_result("register {} {} {} {}".format(name, password, email, phone),
                                        10, RE_REGISTER)
            if result != '-1':
                user_id = result
                result = backend.get_result("query_profile {}".format(user_id),
                                            SZ_QUERY_PROFILE, RE_QUERY_PROFILE).split(' ')
                flask.session[S_CURRENT_USER] = user_id
                flask.session[S_NAME] = name
                flask.session[S_EMAIL] = email
                flask.session[S_PHONE] = phone
                flask.session[S_ADMINISTRATOR] = result[3] == '2'
                flask.session[S_SUCCESS_MESSAGE] = '您的用户ID是 {} ，请牢记'.format(user_id)
            else:
                flask.session[S_ERR_MESSAGE] = E_REGISTER_REJECTED
        except ConnectionRefusedError:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
        except socket.timeout:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
        except SyntaxError:
            flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        flask.session[S_SET_NAME] = name
        flask.session[S_SET_EMAIL] = email
        flask.session[S_SET_PHONE] = phone
        return flask.redirect(flask.url_for('register', _method='GET'))
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            name = flask.session[S_SET_NAME]
            email = flask.session[S_SET_EMAIL]
            phone = flask.session[S_SET_PHONE]
            flask.session.pop(S_ERR_MESSAGE)
            flask.session.pop(S_SET_NAME)
            flask.session.pop(S_SET_EMAIL)
            flask.session.pop(S_SET_PHONE)
            return flask.render_template('register.html', fail_alert=True, message=message,
                                         set_name=name, set_email=email, set_phone=phone)
        elif S_SUCCESS_MESSAGE in flask.session:
            message = flask.session[S_SUCCESS_MESSAGE]
            name = flask.session[S_SET_NAME]
            email = flask.session[S_SET_EMAIL]
            phone = flask.session[S_SET_PHONE]
            flask.session.pop(S_SUCCESS_MESSAGE)
            flask.session.pop(S_SET_NAME)
            flask.session.pop(S_SET_EMAIL)
            flask.session.pop(S_SET_PHONE)
            return flask.render_template('register.html', success_alert=True, message=message,
                                         set_name=name, set_email=email, set_phone=phone)
        else:
            return flask.render_template('register.html')


@app.route('/main_page')
def main_page():
    if flask.session.get(S_VERIFY) != 'main_page':
        flask.session[S_VERIFY] = 'none'
    if not S_CURRENT_USER in flask.session:
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('main_page.html',
                                 username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])


@app.route('/order', methods=['GET', 'POST'])
def order():
    if flask.session.get(S_VERIFY) != 'order':
        flask.session[S_VERIFY] = 'none'
    if not S_CURRENT_USER in flask.session:
        return flask.redirect(flask.url_for('login'))
    if flask.request.method == 'POST':
        if not ('id' in flask.request.args and 'from' in flask.request.args
                and 'to' in flask.request.args and 'date' in flask.request.args):
            flask.session[S_ERR_MESSAGE] = E_INVALID_REQUEST
            return flask.redirect(flask.url_for('order', _method='GET'))
        train_id = flask.request.args['id']
        from_ = flask.request.args['from']
        to = flask.request.args['to']
        date = flask.request.args['date']
        num = flask.request.form['num']
        kind = flask.request.form['kind']
        try:
            result = backend.get_result("buy_ticket {} {} {} {} {} {} {}".format(flask.session[S_CURRENT_USER], num,
                                                                                 train_id, from_, to, date, kind),
                                        SZ_BUY_TICKET, RE_BUY_TICKET)
            if result == '1':
                flask.session[S_SUCCESS_MESSAGE] = '订购成功'
                return flask.redirect(flask.url_for('ordered', _method='GET'))
            else:
                flask.session[S_ERR_MESSAGE] = E_REGISTER_REJECTED
        except ConnectionRefusedError:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
        except socket.timeout:
            flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
        except SyntaxError:
            flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        return flask.redirect(flask.url_for('order', _method='GET'))
    elif flask.request.method == 'GET' and 'id' in flask.request.args and 'from' in flask.request.args \
            and 'to' in flask.request.args and 'date' in flask.request.args:
        train_id = flask.request.args['id']
        from_ = flask.request.args['from']
        to = flask.request.args['to']
        date = flask.request.args['date']
        try:
            result = backend.get_result("query_ticket {} {} {} {}".format(from_, to, date, CATALOG_ALL),
                                        SZ_QUERY_TICKET, RE_QUERY_TICKET)
            if result == '-1':
                return flask.render_template('order_confirm.html', fail_alert=True, message=E_ORDER_NONE,
                                             username=flask.session[S_NAME],
                                             administrator=flask.session[S_ADMINISTRATOR])
            else:
                for ticket_str in result.split('    '):
                    new_ticket = SingleTicket()
                    [new_ticket.id_, new_ticket.name, new_ticket.catalog, new_ticket.from_, new_ticket.from_date,
                     new_ticket.from_time, new_ticket.to, new_ticket.to_date, new_ticket.to_time, ticket_info_str] = \
                        ticket_str.split('   ')
                    if new_ticket.id_ != train_id:
                        continue
                    new_ticket.tickets = []
                    for single_ticket_str in ticket_info_str.split('  '):
                        new_ticket_info = TicketInfo()
                        [new_ticket_info.kind, new_ticket_info.num, new_ticket_info.price] = single_ticket_str.split(
                            ' ')
                        new_ticket.tickets.append(new_ticket_info)
                    return flask.render_template('order_confirm.html', success=True, train_name=new_ticket.name,
                                                 selected_kind=new_ticket.tickets[0].kind,
                                                 from0=new_ticket.from_, from1=new_ticket.from_date,
                                                 from2=new_ticket.from_time,
                                                 to0=new_ticket.to, to1=new_ticket.to_date, to2=new_ticket.to_time,
                                                 tickets=new_ticket.tickets,
                                                 username=flask.session[S_NAME],
                                                 administrator=flask.session[S_ADMINISTRATOR])
                return flask.render_template('order_confirm.html', fail_alert=True, message=E_ORDER_NONE,
                                             username=flask.session[S_NAME],
                                             administrator=flask.session[S_ADMINISTRATOR])
        except ConnectionRefusedError:
            return flask.render_template('order_confirm.html', fail_alert=True, message=E_CONNECTION_REFUSED,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
        except socket.timeout:
            return flask.render_template('order_confirm.html', fail_alert=True, message=E_CONNECTION_TIMEOUT,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
        except SyntaxError:
            return flask.render_template('order_confirm.html', fail_alert=True, message=E_BAD_RETURN,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            flask.session.pop(S_ERR_MESSAGE)
            return flask.render_template('order.html', fail_alert=True, message=message,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
        else:
            return flask.render_template('order.html', username=flask.session[S_NAME],
                                         administrator=flask.session[S_ADMINISTRATOR])


@app.route('/ordered', methods=['GET', 'POST'])
def ordered():
    if flask.session.get(S_VERIFY) != 'ordered':
        flask.session[S_VERIFY] = 'ordered'
    if not S_CURRENT_USER in flask.session:
        return flask.redirect(flask.url_for('login'))
    if flask.request.method == 'POST':
        if 'verify_password' in flask.request.form:
            try:
                verify_password = flask.request.form['verify_password']
                result = backend.get_result('login {} {}'.format(flask.session[S_CURRENT_USER], verify_password),
                                            SZ_LOGIN, RE_LOGIN)
                if result == '1':
                    flask.session[S_VERIFY] = 'account'
                else:
                    flask.session[S_ERR_MESSAGE] = E_PASSWORD_ERROR
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        else:
            try:
                train_id = flask.request.form['train_id']
                from_ = flask.request.form['from']
                to = flask.request.form['to']
                date = flask.request.form['date']
                kind = flask.request.form['kind']
                num = flask.request.form['num']
                result = backend.get_result(
                    'refund_ticket {} {} {} {} {} {} {}'.format(flask.session[S_CURRENT_USER], num, train_id, from_, to,
                                                                date, kind), SZ_REFUND_TICKET, RE_REFUND_TICKET)
                if result == '0':
                    flask.session[S_ERR_MESSAGE] = E_REFUND_TICKET_REJECTED
                else:
                    flask.session[S_SUCCESS_MESSAGE] = '退订成功'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        return flask.redirect(flask.url_for('ordered', _method='GET'))
    else:
        if S_SUCCESS_MESSAGE in flask.session:
            message = flask.session[S_SUCCESS_MESSAGE]
            flask.session.pop(S_SUCCESS_MESSAGE)
            return flask.render_template('ordered.html', success_alert=True, message=message,
                                         success_redirect='/ordered', verified=flask.session[S_VERIFY] == 'ordered',
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
        elif S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            flask.session.pop(S_ERR_MESSAGE)
            return flask.render_template('ordered.html', fail_alert=True, message=message,
                                         fail_redirect='/ordered', verified=flask.session[S_VERIFY] == 'ordered',
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR])
        else:
            try:
                result = backend.get_result('query_order {}'.format(flask.session[S_CURRENT_USER]), SZ_QUERY_ORDER,
                                            RE_QUERY_ORDER)
                if result == '-1':
                    return flask.render_template('ordered.html', empty=True, username=flask.session[S_NAME],
                                                 verified=flask.session[S_VERIFY] == 'ordered',
                                                 administrator=flask.session[S_ADMINISTRATOR])
                else:
                    tickets = []
                    for single_str in result.split('  '):
                        new_ticket = BoughtTicket()
                        [new_ticket.train_id, new_ticket.name, new_ticket.from0, new_ticket.from1, new_ticket.from2,
                         new_ticket.to0, new_ticket.to1, new_ticket.to2, new_ticket.kind,
                         new_ticket.num] = single_str.split(' ')
                        tickets.append(new_ticket)
                    return flask.render_template('ordered.html', tickets=tickets, username=flask.session[S_NAME],
                                                 verified=flask.session[S_VERIFY] == 'ordered',
                                                 administrator=flask.session[S_ADMINISTRATOR])
            except ConnectionRefusedError:
                return flask.render_template('ordered.html', empty=True, fail_alert=True, message=E_CONNECTION_REFUSED,
                                             verified=flask.session[S_VERIFY] == 'ordered',
                                             username=flask.session[S_NAME],
                                             administrator=flask.session[S_ADMINISTRATOR])
            except socket.timeout:
                return flask.render_template('ordered.html', empty=True, fail_alert=True, message=E_CONNECTION_TIMEOUT,
                                             verified=flask.session[S_VERIFY] == 'ordered',
                                             username=flask.session[S_NAME],
                                             administrator=flask.session[S_ADMINISTRATOR])
            except SyntaxError:
                return flask.render_template('ordered.html', empty=True, fail_alert=True, message=E_BAD_RETURN,
                                             verified=flask.session[S_VERIFY] == 'ordered',
                                             username=flask.session[S_NAME],
                                             administrator=flask.session[S_ADMINISTRATOR])


@app.route('/account', methods=['GET', 'POST'])
def account():
    edit = 'edit' in flask.request.args
    if flask.session.get(S_VERIFY) != 'account':
        flask.session[S_VERIFY] = 'none'
    if not S_CURRENT_USER in flask.session:
        return flask.redirect(flask.url_for('login'))
    if flask.request.method == 'POST':
        if 'verify_password' in flask.request.form:
            try:
                verify_password = flask.request.form['verify_password']
                result = backend.get_result('login {} {}'.format(flask.session[S_CURRENT_USER], verify_password),
                                            SZ_LOGIN, RE_LOGIN)
                if result == '1':
                    flask.session[S_VERIFY] = 'account'
                else:
                    flask.session[S_ERR_MESSAGE] = E_PASSWORD_ERROR
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        else:
            try:
                user_id = flask.session[S_CURRENT_USER]
                name = flask.request.form['name']
                email = flask.request.form['email']
                phone = flask.request.form['phone']
                password = flask.request.form['new_password']
                result = backend.get_result('modify_profile {} {} {} {} {}'
                                            .format(user_id, password, name, email, phone),
                                            SZ_MODIFY_PROFILE, RE_MODIFY_PROFILE)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '修改成功'
                    flask.session[S_NAME] = name
                    flask.session[S_EMAIL] = email
                    flask.session[S_PHONE] = phone
                    return flask.redirect(flask.url_for('account', _method='GET'))
                else:
                    flask.session[S_ERR_MESSAGE] = '修改失败'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
        return flask.redirect(flask.url_for('account', _method='GET', edit=True))
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            flask.session.pop(S_ERR_MESSAGE)
            return flask.render_template('account.html', fail_alert=True, message=message, edit=edit,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account',
                                         id=flask.session[S_CURRENT_USER],
                                         email=flask.session[S_EMAIL], phone=flask.session[S_PHONE])
        elif S_SUCCESS_MESSAGE in flask.session:
            message = flask.session[S_SUCCESS_MESSAGE]
            flask.session.pop(S_SUCCESS_MESSAGE)
            return flask.render_template('account.html', success_alert=True, message=message, edit=edit,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account',
                                         id=flask.session[S_CURRENT_USER],
                                         email=flask.session[S_EMAIL], phone=flask.session[S_PHONE])
        else:
            return flask.render_template('account.html', edit=edit,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account',
                                         id=flask.session[S_CURRENT_USER],
                                         email=flask.session[S_EMAIL], phone=flask.session[S_PHONE])


@app.route('/train_manage', methods=['GET', 'POST'])
def train_manage():
    if flask.session.get(S_VERIFY) != 'train_manage':
        flask.session[S_VERIFY] = 'none'
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return E_NOT_ADMINISTRATOR
    if flask.request.method == 'POST':
        if 'verify_password' in flask.request.form:
            try:
                verify_password = flask.request.form['verify_password']
                result = backend.get_result('login {} {}'.format(flask.session[S_CURRENT_USER], verify_password),
                                            SZ_LOGIN, RE_LOGIN)
                if result == '1':
                    flask.session[S_VERIFY] = 'train_manage'
                else:
                    flask.session[S_ERR_MESSAGE] = E_PASSWORD_ERROR
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('train_manage', _method='GET'))
        elif 'add_train' in flask.request.form:
            try:
                train_id = flask.request.form['train_id']
                flask.session[S_MANAGED_TRAIN_ID] = train_id
                request_type = flask.request.form['request-type']
                name = flask.request.form['name']
                catalog = flask.request.form['catalog']
                station_cnt = int(flask.request.form['station-cnt'])
                kind_cnt = int(flask.request.form['kind-cnt'])
                result = backend.get_result('{}_train {} {} {} {} {} {} {}'.format(
                    request_type, train_id, name, catalog, station_cnt, kind_cnt,
                    ' '.join(map(lambda j: flask.request.form['kind-' + str(j)], range(0, kind_cnt))),
                    ' '.join(map(lambda i: '{} {} {} {} {}'.format(
                        flask.request.form['station-' + str(i)], flask.request.form['arrive-' + str(i)],
                        flask.request.form['depart-' + str(i)], flask.request.form['stopover-' + str(i)],
                        ' '.join(
                            map(lambda j: flask.request.form['price-' + str(i) + '-' + str(j)], range(0, kind_cnt)))
                    ), range(0, station_cnt)))
                ), SZ_ADD_TRAIN, RE_ADD_TRAIN)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '添加/修改成功'
                else:
                    flask.session[S_ERR_MESSAGE] = '添加/修改失败'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('train_manage', _method='GET'))
        elif 'sale_train' in flask.request.form:
            try:
                train_id = flask.request.form['train_id']
                flask.session[S_MANAGED_TRAIN_ID] = train_id
                result = backend.get_result('sale_train {}'.format(train_id),
                                            SZ_SALE_TRAIN, RE_SALE_TRAIN)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '公开车次成功'
                else:
                    flask.session[S_ERR_MESSAGE] = E_UNKNOWN
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('train_manage', _method='GET'))
    else:
        if S_SUCCESS_MESSAGE in flask.session:
            message = flask.session[S_SUCCESS_MESSAGE]
            flask.session.pop(S_SUCCESS_MESSAGE)
            return flask.render_template('train_manage.html', username=flask.session[S_NAME],
                                         verified=flask.session[S_VERIFY] == 'train_manage',
                                         administrator=flask.session[S_ADMINISTRATOR],
                                         success_alert=True, initial_query=flask.session.get(S_MANAGED_TRAIN_ID),
                                         message=message)
        elif S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            flask.session.pop(S_ERR_MESSAGE)
            return flask.render_template('train_manage.html', username=flask.session[S_NAME],
                                         verified=flask.session[S_VERIFY] == 'train_manage',
                                         administrator=flask.session[S_ADMINISTRATOR],
                                         fail_alert=True, initial_query=flask.session.get(S_MANAGED_TRAIN_ID),
                                         message=message)
        else:
            return flask.render_template('train_manage.html', username=flask.session[S_NAME],
                                         verified=flask.session[S_VERIFY] == 'train_manage',
                                         initial_query=flask.session.get(S_MANAGED_TRAIN_ID),
                                         administrator=flask.session[S_ADMINISTRATOR])


@app.route('/account_manage', methods=['GET', 'POST'])
def account_manage():
    if flask.session.get(S_VERIFY) != 'account_manage':
        flask.session[S_VERIFY] = 'none'
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return E_NOT_ADMINISTRATOR
    if flask.request.method == 'POST':
        if 'verify_password' in flask.request.form:
            try:
                verify_password = flask.request.form['verify_password']
                result = backend.get_result('login {} {}'.format(flask.session[S_CURRENT_USER], verify_password),
                                            SZ_LOGIN, RE_LOGIN)
                if result == '1':
                    flask.session[S_VERIFY] = 'account_manage'
                else:
                    flask.session[S_ERR_MESSAGE] = E_PASSWORD_ERROR
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('account_manage', _method='GET'))
        elif 'modify_profile' in flask.request.form:
            try:
                user_id = flask.session[S_MANAGED_USER_ID]
                name = flask.request.form['name']
                email = flask.request.form['email']
                phone = flask.request.form['phone']
                password = flask.request.form['new_password']
                result = backend.get_result('modify_profile {} {} {} {} {}'
                                            .format(user_id, password, name, email, phone),
                                            SZ_MODIFY_PROFILE, RE_MODIFY_PROFILE)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '修改成功'
                else:
                    flask.session[S_ERR_MESSAGE] = '修改失败'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('account_manage', _method='GET'))
        elif 'refund_ticket' in flask.request.form:
            try:
                user_id = flask.session[S_MANAGED_USER_ID]
                train_id = flask.request.form['train_id']
                from_ = flask.request.form['from']
                to = flask.request.form['to']
                date = flask.request.form['date']
                kind = flask.request.form['kind']
                num = flask.request.form['num']
                result = backend.get_result(
                    'refund_ticket {} {} {} {} {} {} {}'.format(user_id, num, train_id, from_, to,
                                                                date, kind), SZ_REFUND_TICKET, RE_REFUND_TICKET)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '退订成功'
                else:
                    flask.session[S_ERR_MESSAGE] = '退订失败'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('account_manage', _method='GET'))
        elif 'buy_ticket' in flask.request.form:
            train_id = flask.request.form['train_id']
            from_ = flask.request.form['depart']
            to = flask.request.form['arrive']
            date = flask.request.form['date']
            num = flask.request.form['num']
            kind = flask.request.form['kind']
            try:
                result = backend.get_result("buy_ticket {} {} {} {} {} {} {}".format(flask.session[S_CURRENT_USER], num,
                                                                                     train_id, from_, to, date, kind),
                                            SZ_BUY_TICKET, RE_BUY_TICKET)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '添加成功'
                else:
                    flask.session[S_ERR_MESSAGE] = '添加失败'
            except ConnectionRefusedError:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_REFUSED
            except socket.timeout:
                flask.session[S_ERR_MESSAGE] = E_CONNECTION_TIMEOUT
            except SyntaxError:
                flask.session[S_ERR_MESSAGE] = E_BAD_RETURN
            return flask.redirect(flask.url_for('account_manage', _method='GET'))
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return E_NOT_ADMINISTRATOR
    if S_SUCCESS_MESSAGE in flask.session:
        message = flask.session[S_SUCCESS_MESSAGE]
        flask.session.pop(S_SUCCESS_MESSAGE)
        return flask.render_template('account_manage.html', username=flask.session[S_NAME],
                                     verified=flask.session[S_VERIFY] == 'account_manage',
                                     administrator=flask.session[S_ADMINISTRATOR],
                                     initial_query=flask.session[S_MANAGED_USER_ID], success_alert=True,
                                     message=message)
    elif S_ERR_MESSAGE in flask.session:
        message = flask.session[S_ERR_MESSAGE]
        flask.session.pop(S_ERR_MESSAGE)
        return flask.render_template('account_manage.html', username=flask.session[S_NAME],
                                     verified=flask.session[S_VERIFY] == 'account_manage',
                                     administrator=flask.session[S_ADMINISTRATOR],
                                     initial_query=flask.session[S_MANAGED_USER_ID], fail_alert=True,
                                     message=message)
    else:
        return flask.render_template('account_manage.html', username=flask.session[S_NAME],
                                     verified=flask.session[S_VERIFY] == 'account_manage',
                                     administrator=flask.session[S_ADMINISTRATOR])


@app.route('/ajax_query_profile')
def ajax_query_profile():
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return 'document.body.innerText = "{}"'.format(E_NOT_ADMINISTRATOR)
    if not 'user_id' in flask.request.args:
        return flask.render_template('ajax_bad_request.js', info=E_INVALID_REQUEST)
    user_id = flask.request.args['user_id']
    flask.session[S_MANAGED_USER_ID] = user_id
    try:
        result = backend.get_result("query_profile {}".format(user_id), SZ_QUERY_PROFILE, RE_QUERY_PROFILE_OR_NONE)
        if result == '0':
            return flask.render_template('ajax_query_profile.js', not_exist=True, user_id=user_id)
        else:
            [name, email, phone, administrator] = result.split(' ')
            result = backend.get_result('query_order {}'.format(user_id), SZ_QUERY_ORDER, RE_QUERY_ORDER)
            if result == '-1':
                return flask.render_template('ajax_query_profile.js', user_id=user_id, name=name, email=email,
                                             phone=phone, administrator=administrator == '2', empty=True)
            else:
                tickets = []
                for single_str in result.split('  '):
                    new_ticket = BoughtTicket()
                    [new_ticket.train_id, new_ticket.name, new_ticket.from0, new_ticket.from1, new_ticket.from2,
                     new_ticket.to0, new_ticket.to1, new_ticket.to2, new_ticket.kind,
                     new_ticket.num] = single_str.split(' ')
                    tickets.append(new_ticket)
                return flask.render_template('ajax_query_profile.js', user_id=user_id, name=name, email=email,
                                             phone=phone, administrator=administrator == '2', tickets=tickets)
    except ConnectionRefusedError:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_REFUSED)
    except socket.timeout:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_TIMEOUT)
    except SyntaxError:
        return flask.render_template('ajax_exception.js', info=E_BAD_RETURN)


@app.route('/ajax_modify_privilege')
def ajax_modify_privilege():
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return 'document.body.innerText = "{}"'.format(E_NOT_ADMINISTRATOR)
    if not 'target' in flask.request.args:
        return flask.render_template('ajax_bad_request.js', info=E_INVALID_REQUEST)
    user_id = flask.request.args['target']
    try:
        result = backend.get_result("modify_privilege {} {} 2".format(flask.session[S_CURRENT_USER], user_id),
                                    SZ_MODIFY_PRIVILEGE, RE_MODIFY_PRIVILEGE)
        if result == '0':
            return flask.render_template('ajax_modify_privilege.js', fail=True)
        else:
            return flask.render_template('ajax_modify_privilege.js', user_id=user_id)
    except ConnectionRefusedError:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_REFUSED)
    except socket.timeout:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_TIMEOUT)
    except SyntaxError:
        return flask.render_template('ajax_exception.js', info=E_BAD_RETURN)


@app.route('/ajax_query_ticket')
def ajax_query_ticket():
    if not 'from' in flask.request.args or not 'to' in flask.request.args or not 'date' in flask.request.args or not 'catalog' in flask.request.args:
        return flask.render_template('ajax_bad_request.js', info=E_INVALID_REQUEST)
    _from = flask.request.args['from']
    to = flask.request.args['to']
    date = flask.request.args['date']
    catalog = flask.request.args['catalog']
    if 'transfer' in flask.request.args:
        word = 'transfer'
    else:
        word = 'ticket'
    if _from == to:
        return flask.render_template('ajax_query_ticket.js', error_info=E_QUERY_TICKET_SAME_STATION)
    try:
        result = backend.get_result("query_{} {} {} {} {}".format(word, _from, to, date, catalog),
                                    SZ_QUERY_TICKET, RE_QUERY_TICKET)
        if result == '-1':
            return flask.render_template('ajax_query_ticket.js', error_info=E_QUERY_TICKET_NONE)
        else:
            ticket = []
            for ticket_str in result.split('    '):
                new_ticket = SingleTicket()
                [new_ticket.id_, new_ticket.name, new_ticket.catalog, new_ticket.from_, new_ticket.from_date,
                 new_ticket.from_time, new_ticket.to, new_ticket.to_date, new_ticket.to_time, ticket_info_str] = \
                    ticket_str.split('   ')
                new_ticket.tickets = []
                for single_ticket_str in ticket_info_str.split('  '):
                    new_ticket_info = TicketInfo()
                    [new_ticket_info.kind, new_ticket_info.num, new_ticket_info.price] = single_ticket_str.split(' ')
                    new_ticket.tickets.append(new_ticket_info)
                ticket.append(new_ticket)
            return flask.render_template('ajax_query_ticket.js', ticket_list=ticket,
                                         transfer='transfer' in flask.request.args)
    except ConnectionRefusedError:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_REFUSED)
    except socket.timeout:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_TIMEOUT)
    except SyntaxError:
        return flask.render_template('ajax_exception.js', info=E_BAD_RETURN)


@app.route('/ajax_query_train')
def ajax_query_train():
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return 'document.body.innerText = "{}"'.format(E_NOT_ADMINISTRATOR)
    if not 'train_id' in flask.request.args:
        return flask.render_template('ajax_bad_request.js', info=E_INVALID_REQUEST)
    query_id = flask.request.args['train_id']
    try:
        result = backend.get_result('query_train {}'.format(query_id), SZ_QUERY_TRAIN, RE_QUERY_TRAIN)
        if result == '0':
            return flask.render_template('ajax_query_train.js', not_exsit=True, train_id=query_id)
        else:
            [train_info, ticket_info] = result.split('    ')
            [sold, train_id, name, catalog, all_kind] = train_info.split('  ')
            kinds = all_kind.split(' ')
            stations = []
            for station_str in ticket_info.split('   '):
                new_station = SingleStation()
                [new_station.name, new_station.arrive, new_station.depart, new_station.stopover,
                 all_price] = station_str.split('  ')
                new_station.prices = all_price.split(' ')
                stations.append(new_station)
            return flask.render_template('ajax_query_train.js', train_id=train_id, name=name, catalog=catalog,
                                         kinds=kinds, stations=stations, sold=sold == '1')
    except ConnectionRefusedError:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_REFUSED)
    except socket.timeout:
        return flask.render_template('ajax_exception.js', info=E_CONNECTION_TIMEOUT)
    except SyntaxError:
        return flask.render_template('ajax_exception.js', info=E_BAD_RETURN)


@app.route('/station_list_0')
def station_list_0():
    return flask.send_from_directory('static', 'station_list_0.txt')


@app.route('/station_list_2')
def station_list_2():
    return flask.send_from_directory('static', 'station_list_2.txt')


@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory('static', 'favicon.ico')


app.config.from_object('config')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083, debug=True)
