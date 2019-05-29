import socket, re

back_end = ("127.0.0.1", 5009)


def get_result(info, buff_size, result_validator):
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
