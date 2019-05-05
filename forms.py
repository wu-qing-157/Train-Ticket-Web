from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp
from const import *


class LoginForm(FlaskForm):
    id = StringField(validators=[Regexp(r'^{}$'.format(RE_USER_ID), message="用户ID不合法")])
    password = PasswordField(validators=[Regexp(r'^{}$'.format(RE_PASSWORD), message="密码不合法")])


class RegisterForm(FlaskForm):
    id = StringField(default="ID将自动生成...")
    password = PasswordField(validators=[Regexp(r'^{}$'.format(RE_PASSWORD), message="密码长度必须在6-20位，可以包括数字、字母、符号")])
    password_repeat = PasswordField(validators=[EqualTo('password', message="两次输入的密码不一致")])
    name = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_NAME)), message="姓名长度必须在1-10位，且不包括空格")])
    email = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_EMAIL)), message="请输入正确的邮箱地址")])
    phone = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_PHONE)), message="请输入正确的电话号码")])


class AccountForm(FlaskForm):
    id = StringField()
    name = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_NAME)), message="姓名长度必须在1-10位，且不包括空格")])
    email = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_EMAIL)), message="请输入正确的邮箱地址")])
    phone = StringField(validators=[Regexp(r'^{}$'.format(Regexp(RE_PHONE)), message="请输入正确的电话号码")])
    modify_password = BooleanField()
    new_password = PasswordField(
        validators=[Regexp(r'^({})?$'.format(RE_PASSWORD), message="密码长度必须在6-20位，可以包括数字、字母、符号")])
    new_password_repeat = PasswordField(validators=[EqualTo('new_password', message="两次输入的密码不一致")])
    def __init__(self, id_t, name_t, email_t, phone_t, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.id.data = id_t
        self.name.data = name_t
        self.email.data = email_t
        self.phone.data = phone_t


class VerifyForm(FlaskForm):
    verify_password = PasswordField(validators=[DataRequired()])
