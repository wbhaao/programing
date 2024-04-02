from socket import *

Host = '127.0.0.1'
Port = 9999

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_socket.bind((Host,Port))

print("listening..")
server_socket.listen()

client_socket, addr = server_socket.accept()
print('Connected by',addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received from",addr,data.decode())
    client_socket.sendall(data)

client_socket.close()
server_socket.close()