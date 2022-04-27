import socket
from cryptography.fernet import Fernet


key = b'p7GvOQ_uEvKUPfeWPCeXG7LQyP0LpqMp09qbW7xCxps='
f = Fernet(key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen()


while True:
    connect, addr = sock.accept()
    connect.send(f.encrypt(b"You've connected....")) # here we encrypt a message before sending it to the client

    data = connect.recv(1024)
    plaintext = f.decrypt(data) # here we decrypt the ciphertext sent from the client
    print(plaintext.decode())
    connect.close()
