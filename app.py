import flask, socket

import forms

back_end = ("127.0.0.1", 8081)
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    global sk
    form = forms.LoginForm()
    if form.validate_on_submit():
        user_id = flask.request.form['id']
        password = flask.request.form['password']
        app.logger.debug("login {} {}".format(user_id, password))
        try:
            sk = socket.socket()
            sk.settimeout(10)
            sk.connect(back_end)
            sk.sendall(bytes("login {} {}".format(user_id, password), encoding='utf-8'))
            result = str(sk.recv(1024).strip(), encoding='utf-8')
            app.logger.info("login result {}".format(result))
            if result == '1':
                flask.session['current_user'] = user_id
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
        finally:
            if sk:
                sk.close()
    return flask.render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global sk
    form = forms.RegisterForm()
    if form.validate_on_submit():
        password = flask.request.form['password']
        name = flask.request.form['name']
        email = flask.request.form['email']
        phone = flask.request.form['phone']
        try:
            sk = socket.socket()
            sk.settimeout(10)
            sk.connect(back_end)
            sk.sendall(bytes("register {} {} {} {}".format(password, name, email, phone), encoding='utf-8'))
            result = str(sk.recv(1024).strip(), encoding='utf-8')
            app.logger.info("register result {}".format(result))
            if result != '0':
                user_id = result
                flask.session['current_user'] = user_id
                return flask.render_template('register.html',
                                             form=form,
                                             success_alert=True,
                                             user_id=user_id)
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
        finally:
            if sk:
                sk.close()
    if flask.request.method == 'POST':
        for field, message in form.errors.items():
            app.logger.info('{} {}'.format(field, message))
        form.password.data = flask.request.form['password']
    return flask.render_template('register.html', form=form)


@app.route('/main_page')
def main_page():
    return flask.render_template('main_page.html', username=flask.session['current_user'])


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(host="0.0.0.0", port=8083, debug=True)
