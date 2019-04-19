from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    id = StringField('id', default="ID将自动生成...")
    password = PasswordField('password', validators=[DataRequired()])
    password_repeat = PasswordField('password_repeat',
                                    validators=[DataRequired(), EqualTo('password', message="两次输入的密码不一致")])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email(message="邮箱地址不合法")])
    phone = StringField('phone', validators=[DataRequired()])


class AccountForm(FlaskForm):
    def __init__(self, id_t, name_t, email_t, phone_t):
        self.id = StringField('id', default=id_t)
        self.old_password = PasswordField('old_password', validators=[DataRequired()])
        self.name = StringField('name', default=name_t, validators=[DataRequired()])
        self.email = StringField('email', default=email_t, validators=[DataRequired()])
        self.phone = StringField('phone', default=phone_t, validators=[DataRequired()])
        self.new_password = PasswordField('new_password')
        self.new_password_repeat = PasswordField('new_password_repeat')
