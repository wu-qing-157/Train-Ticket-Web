from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    id = StringField('id', default="ID将自动生成...")
    password = PasswordField('password', validators=[DataRequired()])
    password_repeat = PasswordField('password_repeat', validators=[DataRequired(), EqualTo('password', message="两次输入的密码不一致")])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email(message="邮箱地址不合法")])
    phone = StringField('phone', validators=[DataRequired()])
