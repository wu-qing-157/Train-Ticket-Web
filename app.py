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
        username = flask.request.form['username']
        password = flask.request.form['password']
        app.logger.debug("login {} {}".format(username, password))
        try:
            sk = socket.socket()
            sk.connect(back_end)
            sk.sendall(bytes("login {} {}".format(username, password), encoding='utf-8'))
            sk.settimeout(10)
            result = str(sk.recv(1024).strip(), encoding='utf-8')
            app.logger.info("login result {}".format(result))
            if result == 'Success':
                flask.session['current_user'] = username
                return flask.redirect(flask.url_for('main_page'))
            elif result == 'Fail':
                return flask.render_template('login_info.html', title='登录失败', messages='用户名和密码不匹配')
                # flask.flash('登录失败')
                # return flask.redirect(flask.url_for('login'))
            else:
                flask.flash('未知错误')
                return flask.redirect(flask.url_for('login'))
        except ConnectionRefusedError:
            flask.flash('无法连接到服务器')
            return flask.redirect(flask.url_for('login'))
        except socket.timeout:
            flask.flash('无法连接到服务器')
            return flask.redirect(flask.url_for('login'))
        finally:
            sk.close()
    return flask.render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global sk
    form = forms.RegisterForm()
    if form.validate_on_submit():
        password = flask.request.form['password']
    if flask.request.method == 'POST':
        form.password.data = flask.request.form['password']
    return flask.render_template('register.html', form=form)


@app.route('/main_page')
def main_page():
    return flask.render_template('main_page.html', username=flask.session['current_user'])


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(host="127.0.0.1", port=8083, debug=True)
