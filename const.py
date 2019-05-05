S_CURRENT_USER = 'current_user'
S_NAME = 'name'
S_EMAIL = 'email'
S_PHONE = 'phone'
S_ADMINISTRATOR = 'administrator'
S_ERR_MESSAGE = 'err_message'
S_SUCCESS_MESSAGE = 'success_message'
S_VERIFY = 'verified'
S_PASSWORD = 'password'
S_ACCOUNT_EDIT = 'edit'
S_SET_USER_ID = 'set_id'
S_SET_NAME = 'set_name'
S_SET_EMAIL = 'set_email'
S_SET_PHONE = 'set_phone'

SZ_LOGIN = 10
SZ_REGISTER = 10
SZ_QUERY_PROFILE = 100
SZ_MODIFY_PROFILE = 10

RE_USER_ID = r'\d{4,20}'
RE_PASSWORD = r'[\u0020-\u007e]{6,20}'
RE_NAME = r'\S{1,10}'
RE_EMAIL = r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
RE_PHONE = r'\+?[0-9]{3,}'

RE_LOGIN = r'^[01]$'
RE_REGISTER = r'^(-1)|({})$'.format(RE_USER_ID)
RE_QUERY_PROFILE = r'^{} {} {} [12]$'.format(RE_NAME, RE_EMAIL, RE_PHONE)
RE_MODIFY_PROFILE = r'^[01]$'

E_PASSWORD_NOT_MATCH = '用户名或密码错误'
E_PASSWORD_ERROR = '密码错误'
E_CONNECTION_REFUSED = '无法连接到服务器'
E_CONNECTION_TIMEOUT = '服务器超时'
E_BAD_RETURN = '服务器返回数据时出现异常'
E_REGISTER_REJECTED = '当前拒绝注册新用户'
