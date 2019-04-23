import flask, socket

import forms, backend

app = flask.Flask(__name__)


@app.route('/')
def index():
    if 'current_user' in flask.session:
        return flask.redirect(flask.url_for('main_page'))
    else:
        return flask.redirect(flask.url_for('login'))


@app.route('/logout')
def logout():
    flask.session.pop('current_user')
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user_id = flask.request.form['id']
        password = flask.request.form['password']
        app.logger.debug("login {} {}".format(user_id, password))
        try:
            result = backend.get_result("login {} {}".format(user_id, password), 1024)
            app.logger.info("login result {}".format(result))
            if result == '1':
                flask.session['current_user'] = user_id
                result = backend.get_result("query_profile {}".format(flask.session['current_user']), 1024).split(' ')
                name = result[0]
                privilege = result[3]
                flask.session['current_user'] = user_id
                if privilege == '2':
                    flask.session['username'] = name
                    flask.session['administrator'] = True
                elif privilege == '1':
                    flask.session['username'] = name
                    flask.session['administrator'] = False
                else:
                    return flask.render_template('login.html',
                                                 form=form,
                                                 fail_alert=True,
                                                 message='未知错误')
                return flask.redirect(flask.url_for('main_page'))
            elif result == '0':
                return flask.render_template('login.html',
                                             form=form,
                                             show_alert=True,
                                             message='用户名和密码不匹配')
            else:
                flask.flash('未知错误')
                return flask.render_template('login.html',
                                             form=form,
                                             show_alert=True,
                                             message='未知错误')
        except ConnectionRefusedError:
            return flask.render_template('login.html',
                                         form=form,
                                         show_alert=True,
                                         message='无法连接到登录服务器')
        except socket.timeout:
            return flask.render_template('login.html',
                                         form=form,
                                         show_alert=True,
                                         message='登录服务器超时')
    return flask.render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        password = flask.request.form['password']
        name = flask.request.form['name']
        email = flask.request.form['email']
        phone = flask.request.form['phone']
        try:
            result = backend.get_result("register {} {} {} {}".format(name, password, email, phone), 1024)
            if result != '0':
                user_id = result
                result = backend.get_result("query_profile {}".format(user_id), 1024).split(' ')
                privilege = result[3]
                flask.session['current_user'] = user_id
                if privilege == '2':
                    flask.session['username'] = name
                    flask.session['administrator'] = True
                    return flask.render_template('register.html',
                                                 form=form,
                                                 success_alert=True,
                                                 user_id=user_id)
                elif privilege == '1':
                    flask.session['username'] = name
                    flask.session['administrator'] = False
                else:
                    return flask.render_template('register.html',
                                                 form=form,
                                                 fail_alert=True,
                                                 message='未知错误')
            else:
                return flask.render_template('register.html',
                                             form=form,
                                             fail_alert=True,
                                             message='未知错误')
        except ConnectionRefusedError:
            return flask.render_template('register.html',
                                         form=form,
                                         fail_alert=True,
                                         message='无法连接到登录服务器')
        except socket.timeout:
            return flask.render_template('register.html',
                                         form=form,
                                         fail_alert=True,
                                         message='登录服务器连接超时')
    if flask.request.method == 'POST':
        msg = ''
        for field, message in form.errors.items():
            for item in message:
                if msg != '':
                    msg = msg + '；'
                msg = msg + item
        return flask.render_template('register.html',
                                     form=form,
                                     fail_alert=True,
                                     message=msg)
    return flask.render_template('register.html', form=form)


@app.route('/main_page')
def main_page():
    if not 'current_user' in flask.session:
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('main_page.html',
                                 username=flask.session['username'],
                                 administrator=flask.session['administrator'])


@app.route('/account')
def account():
    if not 'current_user' in flask.session:
        return flask.redirect(flask.url_for('login'))
    [username, email, phone, _] = backend.get_result(
        'query_profile {}'.format(flask.session['current_user']), 1024).split(' ')
    form = forms.AccountForm(flask.session['current_user'], username, email, phone)
    verify_form = forms.VerifyForm()
    return flask.render_template('account.html',
                                 username=username,
                                 form=form,
                                 verify_form=verify_form)


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    message = flask.session['to_verify_message']
    warning = flask.session['to_verify_warning']
    form = forms.VerifyForm()
    if flask.request.method == 'POST':
        try:
            result = backend.get_result(
                "login {} {}".format(flask.session['current_user'], flask.request.form['password']), 1024)
            if result == '1':
                what = flask.session['to_verify']
                flask.session[what] = True
            else:
                return flask.render_template('verify.html',
                                             message=message,
                                             warning=warning,
                                             form=form,
                                             error=True)
        except ConnectionRefusedError:
            return flask.render_template('verify.html',
                                         message=message,
                                         warning=warning,
                                         form=form,
                                         error=True)
        except socket.timeout:
            return flask.render_template('verify.html',
                                         message=message,
                                         warning=warning,
                                         form=form,
                                         error=True)
    return flask.render_template('verify.html',
                                 message=message,
                                 warning=warning,
                                 form=form)


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(host="0.0.0.0", port=8083, debug=True)
