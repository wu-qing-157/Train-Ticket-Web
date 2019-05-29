import socket, socketserver
import threading
from subprocess import Popen, PIPE

stdout_lock = threading.Lock()


def format_address(address):
    return "{}:{}".format(address[0], address[1])


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        global stdout_lock
        try:
            if stdout_lock.acquire():
                print("(Connected) {}".format(format_address(self.client_address)))
                connection = self.request
                connection.settimeout(60)
                try:
                    recv = connection.recv(1024)
                    print("--- Receive   --- <<< {}".format(str(recv, encoding="utf-8")))
                    try:
                        tosend = bytes(input("--- Response? --- >>> "), encoding="utf-8")
                        connection.sendall(tosend)
                        print("(Send) {} {}".format(format_address(self.client_address), str(tosend, encoding="utf-8")))
                    except BrokenPipeError:
                        print("(Error) Client disconnected")
                except socket.timeout:
                    print("(Timeout) {}".format(format_address(self.client_address)))
        finally:
            stdout_lock.release()
        print("")


if __name__ == "__main__":
    # exe = Popen(['./server'], shell = True, stdin = PIPE, stdout = PIPE)
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 5009), MyServer)
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 8081), MyServer)
    server.serve_forever()
