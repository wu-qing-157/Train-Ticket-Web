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
    id = StringField('id')
    old_password = PasswordField('old_password', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    new_password = PasswordField('new_password')
    new_password_repeat = PasswordField('new_password_repeat')
    def __init__(self, id_t, name_t, email_t, phone_t, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.id.data = id_t
        self.name.data = name_t
        self.email.data = email_t
        self.phone.data = phone_t


class VerifyForm(FlaskForm):
    verify_password = PasswordField('password', validators=[DataRequired()])
