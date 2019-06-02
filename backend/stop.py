import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 5009))
sk.sendall(bytes("exit", encoding='utf-8'))
print(str(sk.recv(1024), encoding='utf-8'))
sk.close()
