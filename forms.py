from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    id = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    id = StringField(default="ID将自动生成...")
    password = PasswordField(validators=[DataRequired()])
    password_repeat = PasswordField(validators=[DataRequired(), EqualTo('password', message="两次输入的密码不一致")])
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(message="邮箱地址不合法")])
    phone = StringField(validators=[DataRequired()])


class AccountForm(FlaskForm):
    id = StringField()
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired()])
    modify_password = BooleanField()
    new_password = PasswordField()
    new_password_repeat = PasswordField(validators=[EqualTo('new_password', message="两次输入的密码不一致")])
    def __init__(self, id_t, name_t, email_t, phone_t, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.id.data = id_t
        self.name.data = name_t
        self.email.data = email_t
        self.phone.data = phone_t


class VerifyForm(FlaskForm):
    verify_password = PasswordField(validators=[DataRequired()])
