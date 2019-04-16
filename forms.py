from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(Form):
    password = PasswordField('password', validators=[DataRequired()])
    password_repeat = PasswordField('password_repeat', validators=[DataRequired(), EqualTo('password', message="两次输入的密码不一致")])
    email = StringField('email', validators=[DataRequired(), Email(message="邮箱地址不合法")])
    phone = StringField('phone', validators=[DataRequired()])
