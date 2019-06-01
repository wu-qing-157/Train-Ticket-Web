import socket

obj = socket.socket()
obj.connect(("127.0.0.1", 8081))

try:
    while True:
        try:
            inp = input("                                  >>> ")
            if inp == "":
                break
            obj.sendall(bytes(inp, encoding = "utf-8"))
            print("{} <<< ".format(str(obj.recv(1024), encoding = "utf-8")))
        except EOFError:
            break
finally:
    obj.close()

