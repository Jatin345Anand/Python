import socket

clientSocket = socket.socket()

port = 9999
host_ip = '127.0.0.1'

clientSocket.connect((host_ip, port))

data = clientSocket.recv(1024)
print("Server ::",data.decode())

while True:
    message = input("Enter your message : ")
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024)
    print("Server ::", data.decode())

clientSocket.close()