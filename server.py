import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen()

while True:
    connect, addr = sock.accept()
    connect.send("You've connected....".encode())
    data = connect.recv(1024)
    print(data.decode())
    connect.close()
