S_CURRENT_USER = 'current_user'
S_NAME = 'name'
S_EMAIL = 'email'
S_PHONE = 'phone'
S_ADMINISTRATOR = 'administrator'
S_ERR_MESSAGE = 'err_message'
S_SUCCESS_MESSAGE = 'success_message'
S_VERIFY = 'verified'
S_SET_USER_ID = 'set_id'
S_SET_NAME = 'set_name'
S_SET_EMAIL = 'set_email'
S_SET_PHONE = 'set_phone'
S_MANAGED_USER_ID = 'managed_user_id'

SZ_LOGIN = 10
SZ_REGISTER = 10
SZ_QUERY_PROFILE = 100
SZ_MODIFY_PROFILE = 10
SZ_MODIFY_PRIVILEGE = 10
SZ_QUERY_TICKET = 8192

RE_USER_ID = r'\d{4,20}'
RE_PASSWORD = r'[\u0021-\u007e]{6,20}'
RE_NAME = r'\S{1,10}'
RE_EMAIL = r'(?!\S{21})\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
RE_PHONE = r'(?!\S{21})\+?[0-9]{3,}'
RE_TRAIN_ID = r'[a-zA-Z0-9]{1,10}'
RE_DATE = r'\d{4}-\d{2}-\d{2}'
RE_TIME = r'\d{2}:\d{2}'
RE_CATALOG = r'[A-Z]'
RE_NUM = r'\d+'
RE_PRICE = r'\S+'
RE_SINGLE_TICKET = r'{}   {}   {}(   {}   {}   {}){}   ({} {} {})(  {} {} {})*' \
    .format(RE_TRAIN_ID, RE_NAME, RE_CATALOG, RE_NAME, RE_DATE, RE_TIME, '{2}', RE_NAME, RE_NUM, RE_PRICE, RE_NAME,
            RE_NUM, RE_PRICE)
RE_SINGLE_STATION = r'{}  {}  {}  {}  {}( {})*' \
    .format(RE_NAME, RE_TIME, RE_TIME, RE_TIME, RE_PRICE, RE_PRICE)

RE_LOGIN = r'^[01]$'
RE_REGISTER = r'^(-1)|({})$'.format(RE_USER_ID)
RE_QUERY_PROFILE = r'^{} {} {} [12]$'.format(RE_NAME, RE_EMAIL, RE_PHONE)
RE_QUERY_PROFILE_OR_NONE = r'^0|({} {} {} [12])$'.format(RE_NAME, RE_EMAIL, RE_PHONE)
RE_MODIFY_PROFILE = r'^[01]$'
RE_MODIFY_PRIVILEGE = r'^[01]$'
RE_QUERY_TICKET = r'^(-1)|({}(    {})*)$'.format(RE_SINGLE_TICKET, RE_SINGLE_TICKET)
RE_QUERY_TRANSFER = r'^{}    {}$'.format(RE_SINGLE_TICKET, RE_SINGLE_TICKET)
RE_QUERY_TRAIN = r'^{}  {}  {}  {}( {})*    {}(   {})*$' \
    .format(RE_TRAIN_ID, RE_NAME, RE_CATALOG, RE_NAME, RE_NAME, RE_SINGLE_TICKET, RE_SINGLE_TICKET)

E_UNKNOWN = '未知错误原因'
E_PASSWORD_NOT_MATCH = '用户名或密码错误'
E_PASSWORD_ERROR = '密码错误'
E_CONNECTION_REFUSED = '无法连接到服务器'
E_CONNECTION_TIMEOUT = '服务器超时'
E_BAD_RETURN = '服务器返回数据时出现异常'
E_REGISTER_REJECTED = '当前拒绝注册新用户'
E_NOT_ADMINISTRATOR = '你没有权限进行这一操作'
E_INVALID_REQUEST = '请求的内容不合法'
E_QUERY_TICKET_SAME_STATION = '出发站和到达站是同一个车站，如果您需要从出发区域前往到达区域，您可以选择步行'
E_QUERY_TICKET_NONE = '没有符合条件的车次'
E_ORDER_NONE = '找不到该车次'

CATALOG_ALL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
