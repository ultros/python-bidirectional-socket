import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

sock.send("Sent from client...".encode())
print(sock.recv(1024).decode())
sock.close()