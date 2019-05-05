from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import EqualTo, Regexp
from const import *


class LoginForm(FlaskForm):
    id = StringField(validators=[Regexp(r'^{}$'.format(RE_USER_ID), message="用户ID不合法")])
    password = PasswordField(validators=[Regexp(r'^{}$'.format(RE_PASSWORD), message="密码错误")])


class RegisterForm(FlaskForm):
    id = StringField(default="ID将自动生成...")
    password = PasswordField(validators=[Regexp(r'^{}$'.format(RE_PASSWORD), message="密码长度必须在6-20位，可以包括数字、字母、符号")])
    password_repeat = PasswordField(validators=[EqualTo('password', message="两次输入的密码不一致")])
    name = StringField(validators=[Regexp(r'^{}$'.format(RE_NAME), message="姓名长度必须在1-10位，且不包括空格")])
    email = StringField(validators=[Regexp(r'^{}$'.format(RE_EMAIL), message="请输入正确的邮箱地址")])
    phone = StringField(validators=[Regexp(r'^{}$'.format(RE_PHONE), message="请输入正确的电话号码")])


class AccountForm(FlaskForm):
    id = StringField()
    name = StringField(validators=[Regexp(r'^{}$'.format(RE_NAME), message="姓名长度必须在1-10位，且不包括空格")])
    email = StringField(validators=[Regexp(r'^{}$'.format(RE_EMAIL), message="请输入正确的邮箱地址")])
    phone = StringField(validators=[Regexp(r'^{}$'.format(RE_PHONE), message="请输入正确的电话号码")])
    modify_password = BooleanField()
    new_password = PasswordField(
        validators=[Regexp(r'^({})?$'.format(RE_PASSWORD), message="密码长度必须在6-20位，可以包括数字、字母、符号")])
    new_password_repeat = PasswordField(validators=[EqualTo('new_password', message="两次输入的密码不一致")])


class VerifyForm(FlaskForm):
    verify_password = PasswordField(validators=[Regexp(r'^{}$'.format(RE_PASSWORD), message="密码错误")])


def get_validator_errors(form):
    err_list = []
    for _, info in form.errors.items():
        err_list += info
    return '；'.join(err_list)
