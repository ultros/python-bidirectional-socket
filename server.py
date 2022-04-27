import socket
from cryptography.fernet import Fernet

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen()
key = b'p7GvOQ_uEvKUPfeWPCeXG7LQyP0LpqMp09qbW7xCxps='
f = Fernet(key)

while True:
    connect, addr = sock.accept()
    connect.send(f.encrypt(b"You've connected...."))

    data = connect.recv(1024)
    plaintext = f.decrypt(data)
    print(plaintext.decode())
    connect.close()
