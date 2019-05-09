import flask, socket

import backend

from const import *

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
                flask.session[S_PASSWORD] = password
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
                flask.session[S_PASSWORD] = password
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


@app.route('/order')
def order():
    return 'order'


@app.route('/ordered')
def ordered():
    return 'ordered'


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
                modify_password = 'modify_password' in flask.request.form
                if modify_password:
                    password = flask.request.form['new_password']
                else:
                    password = flask.session['password']
                result = backend.get_result('modify_profile {} {} {} {} {}'
                                            .format(user_id, password, name, email, phone),
                                            SZ_MODIFY_PROFILE, RE_MODIFY_PROFILE)
                if result == '1':
                    flask.session[S_SUCCESS_MESSAGE] = '修改成功'
                    flask.session[S_NAME] = name
                    flask.session[S_EMAIL] = email
                    flask.session[S_PHONE] = phone
                    flask.session[S_PASSWORD] = password
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


@app.route('/train_manage')
def train_manage():
    return 'train_manage'


@app.route('/account_manage')
def account_manage():
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return E_NOT_ADMINISTRATOR
    return flask.render_template('account_manage.html', username=flask.session[S_NAME],
                                 administrator=flask.session[S_ADMINISTRATOR])


@app.route('/ajax_query_profile')
def ajax_query_profile():
    if not S_ADMINISTRATOR in flask.session or not flask.session[S_ADMINISTRATOR]:
        return 'document.body.innerText = "{}"'.format(E_NOT_ADMINISTRATOR)
    if not 'user_id' in flask.request.args:
        return flask.render_template('ajax_bad_request.jinja', info=E_INVALID_REQUEST)
    user_id = flask.request.args['user_id']
    try:
        result = backend.get_result("query_profile {}".format(user_id), SZ_QUERY_PROFILE, RE_QUERY_PROFILE_OR_NONE)
        if result == '0':
            return flask.render_template('ajax_query_profile.jinja', not_exist=True, user_id=user_id)
        else:
            [name, email, phone, administrator] = result.split(' ')
            return flask.render_template('ajax_query_profile.jinja', user_id=user_id, name=name, email=email,
                                         phone=phone, administrator=administrator)
    except ConnectionRefusedError:
        return flask.render_template('ajax_exception.jinja', info=E_CONNECTION_REFUSED)
    except socket.timeout:
        return flask.render_template('ajax_exception.jinja', info=E_CONNECTION_TIMEOUT)
    except SyntaxError:
        return flask.render_template('ajax_exception.jinja', info=E_BAD_RETURN)


app.config.from_object('config')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083, debug=True)
