import socket, socketserver
import threading
from subprocess import Popen, PIPE

stdout_lock = threading.Lock()

def format_address(address):
    return "{}:{}".format(address[0], address[1])

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("Connect {}".format(format_address(self.client_address)))
        global stdout_lock
        if stdout_lock.acquire():
            try:
                connection = self.request
                connection.settimeout(60)
                recv = connection.recv(1048576)
                print("Receive {} {}".format(format_address(self.client_address), str(recv, encoding = "utf-8")))
                try:
                    exe.stdin.write(recv + bytes('\n', encoding = "utf-8"))
                    exe.stdin.flush()
                    tosend = str(exe.stdout.readline().strip(), encoding = "utf-8").strip()
                    connection.sendall(bytes(tosend, encoding = "utf-8"))
                    print("Send    {} {}".format(format_address(self.client_address), tosend))
                except BrokenPipeError:
                    print("Error   {} Client disconnected".format(format_address(self.client_address)))
            except socket.timeout:
                print("Timeout {}".format(format_address(self.client_address)))
            finally:
                stdout_lock.release()
        print("Finish  {}".format(format_address(self.client_address)))

if __name__ == "__main__":
    exe = Popen(['./code'], bufsize = 1048576, shell = True, stdin = PIPE, stdout = PIPE)
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 5009), MyServer)
    server.serve_forever()

