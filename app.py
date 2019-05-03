import flask, socket

import forms, backend

S_CURRENT_USER = 'current_user'
S_NAME = 'name'
S_EMAIL = 'email'
S_PHONE = 'phone'
S_ADMINISTRATOR = 'administrator'
S_ERR_MESSAGE = 'err_message'
S_SUCCESS_MESSAGE = 'success_message'
S_VERIFY = 'verified'
S_PASSWORD = 'password'
S_ACCOUNT_EDIT = 'edit'
S_SET_USER_ID = 'set_id'
S_SET_NAME = 'set_name'
S_SET_EMAIL = 'set_email'
S_SET_PHONE = 'set_phone'

SZ_LOGIN = 10
SZ_REGISTER = 10
SZ_QUERY_PROFILE = 100
SZ_MODIFY_PROFILE = 10

RE_LOGIN = r'^[01]$'
RE_REGISTER = r'^(-1)|(\d+)$'
RE_QUERY_PROFILE = r'^\S+\s\S+@\S+\s\S+\s[12]$'
RE_MODIFY_PROFILE = r'^[01]$'

E_PASSWORD_NOT_MATCH = '用户名或密码错误'
E_PASSWORD_ERROR = '密码错误'
E_CONNECTION_REFUSED = '无法连接到服务器'
E_CONNECTION_TIMEOUT = '服务器超时'
E_BAD_RETURN = '服务器返回数据时出现异常'
E_REGISTER_REJECTED = '当前拒绝注册新用户'

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
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        user_id = flask.request.form['id']
        password = flask.request.form['password']
        if form.validate_on_submit():
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
        else:
            err_list = []
            for _, info in form.errors.items():
                err_list += info
            flask.session[S_ERR_MESSAGE] = '；'.join(err_list)
        flask.session[S_SET_USER_ID] = user_id
        return flask.redirect(flask.url_for('login', _method='GET'))
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            user_id = flask.session[S_SET_USER_ID]
            flask.session.pop(S_ERR_MESSAGE)
            flask.session.pop(S_SET_USER_ID)
            return flask.render_template('login.html', form=form, show_alert=True, message=message, set_id=user_id)
        else:
            return flask.render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if flask.request.method == 'POST':
        password = flask.request.form['password']
        name = flask.request.form['name']
        email = flask.request.form['email']
        phone = flask.request.form['phone']
        if form.validate_on_submit():
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
        else:
            err_list = []
            for _, info in form.errors.items():
                err_list += info
            flask.session[S_ERR_MESSAGE] = '；'.join(err_list)
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
            return flask.render_template('register.html', form=form, fail_alert=True, message=message,
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
            return flask.render_template('register.html', form=form, success_alert=True, message=message,
                                         set_name=name, set_email=email, set_phone=phone)
        else:
            return flask.render_template('register.html', form=form)


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
    if flask.session.get(S_VERIFY) != 'account':
        flask.session[S_VERIFY] = 'none'
    if not S_CURRENT_USER in flask.session:
        return flask.redirect(flask.url_for('login'))
    form = forms.AccountForm(flask.session[S_CURRENT_USER], flask.session[S_NAME], flask.session[S_EMAIL],
                             flask.session[S_PHONE])
    verify_form = forms.VerifyForm()
    if flask.request.method == 'POST':
        if 'verify_password' in flask.request.form:
            if verify_form.validate_on_submit():
                try:
                    verify_password = flask.request.form['verify_password']
                    result = backend.get_result('login {} {}'.format(flask.session[S_NAME], verify_password),
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
                flask.session[S_ERR_MESSAGE] = '；'.join(verify_form.errors.items())
        else:
            if form.validate_on_submit():
                try:
                    user_id = flask.session[S_CURRENT_USER]
                    name = flask.request.form['name']
                    email = flask.request.form['email']
                    phone = flask.request.form['phone']
                    modify_password = flask.request.form['modify_password'] == 'y'
                    if modify_password:
                        password = flask.request.form['new_password']
                    else:
                        password = flask.session['password']
                    result = backend.get_result('modify_profile {} {} {} {} {}'
                                                .format(user_id, password, name, email, phone),
                                                SZ_QUERY_PROFILE, RE_QUERY_PROFILE)
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
            else:
                err_list = []
                for _, info in form.errors.items():
                    err_list += info
                flask.session[S_ERR_MESSAGE] = '；'.join(err_list)
        flask.session[S_ACCOUNT_EDIT] = True
        return flask.redirect(flask.url_for('account', _method='GET'))
    else:
        if S_ERR_MESSAGE in flask.session:
            message = flask.session[S_ERR_MESSAGE]
            flask.session.pop(S_ERR_MESSAGE)
            return flask.render_template('account.html', form=form, fail_alert=True, message=message, edit=True,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account', verify_form=verify_form)
        elif S_SUCCESS_MESSAGE in flask.session:
            message = flask.session[S_SUCCESS_MESSAGE]
            flask.session.pop(S_SUCCESS_MESSAGE)
            return flask.render_template('account.html', form=form, success_alert=True, message=message, edit=True,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account', verify_form=verify_form)
        else:
            if S_ACCOUNT_EDIT in flask.session:
                edit = True
                flask.session.pop(S_ACCOUNT_EDIT)
            else:
                edit = False
            return flask.render_template('account.html', form=form, edit=edit,
                                         username=flask.session[S_NAME], administrator=flask.session[S_ADMINISTRATOR],
                                         verified=flask.session[S_VERIFY] == 'account', verify_form=verify_form)


@app.route('/train_manage')
def train_manage():
    return 'train_manage'


@app.route('/account_manage')
def account_manage():
    return 'account_manage'


app.config.from_object('config')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083, debug=True)
