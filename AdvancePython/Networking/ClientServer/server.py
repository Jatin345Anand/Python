import socket

mySocket = socket.socket()

port = 9999

mySocket.bind(('localhost',port))

mySocket.listen(5)
print("Waiting for client")

message = "Thanks for connecting with us"
conn, addr = mySocket.accept()
conn.send(message.encode())
print("Client comes...")
print("Client address",addr)
while True:
    data = conn.recv(1024)
    print("Client ::", data.decode())
    message = input("Enter your message : ")
    conn.send(message.encode())

conn.close()