import socket, socketserver
import threading
from subprocess import Popen, PIPE

stdout_lock = threading.Lock()

def format_address(address):
    return "{}:{}".format(address[0], address[1])

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("(Connected) {}".format(format_address(self.client_address)))
        connection = self.request
        connection.settimeout(60)
        while True:
            try:
                recv = connection.recv(1024)
                print("(Receive) {} {}".format(format_address(self.client_address), str(recv, encoding = "utf-8")))

                global stdout_lock
                if stdout_lock.acquire():
                    try:
                        exe.stdin.write(recv + bytes('\n', encoding = "utf-8"))
                        exe.stdin.flush()
                        tosend = exe.stdout.readline().strip()
                        connection.sendall(tosend)
                        print("(Send) {} {}".format(format_address(self.client_address), str(tosend, encoding = "utf-8")))
                    except BrokenPipeError:
                        print("(Error) Client disconnected")
                        break
                    finally:
                        stdout_lock.release()
                else:
                    print("(Error) Server busy")
            except socket.timeout:
                print("(Timeout) {}".format(format_address(self.client_address)))
                break
        print("(Finish) {}".format(format_address(self.client_address)))

if __name__ == "__main__":
    exe = Popen(['./server'], shell = True, stdin = PIPE, stdout = PIPE)
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8081), MyServer)
    server.serve_forever()

