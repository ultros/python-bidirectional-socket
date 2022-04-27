
import socket
from cryptography.fernet import Fernet

key = b'p7GvOQ_uEvKUPfeWPCeXG7LQyP0LpqMp09qbW7xCxps='
f = Fernet(key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
sock.send(f.encrypt(b'test from client'))

data = sock.recv(1024)
plaintext = f.decrypt(data)
print(plaintext.decode())

sock.close()