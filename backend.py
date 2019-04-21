import socket

back_end = ("127.0.0.1", 8081)

def get_result(info, buff_size):
    global sk
    try:
        sk = socket.socket()
        sk.settimeout(10)
        sk.connect(back_end)
        sk.sendall(bytes(info, encoding='utf-8'))
        result = str(sk.recv(buff_size).strip(), encoding='utf-8')
        return result
    finally:
        sk.close()