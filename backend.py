import socket, re

from app import app

back_end = ("127.0.0.1", 8081)


def get_result(info, buff_size, result_validator):
    app.logger.info("Request: {}".format(info.split(' ')[0]))
    global sk
    try:
        sk = socket.socket()
        sk.settimeout(100)
        sk.connect(back_end)
        sk.sendall(bytes(info, encoding='utf-8'))
        result = str(sk.recv(buff_size).strip(), encoding='utf-8')
        if not re.match(result_validator, result):
            raise SyntaxError('Unexpected result')
        return result
    except UnicodeDecodeError:
        raise SyntaxError('Unexpected result')
    finally:
        if sk:
            sk.close()