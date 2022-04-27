import socket
from cryptography.fernet import Fernet

# The key generated below is the shared symmetric "secret key" used to encrypt and decrypt traffic between the hosts.
# This key is shared on the host and the client.
key = b'p7GvOQ_uEvKUPfeWPCeXG7LQyP0LpqMp09qbW7xCxps='
f = Fernet(key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
sock.send(f.encrypt(b'test from client')) # here we have encrypted a message being sent to the server

data = sock.recv(1024)
plaintext = f.decrypt(data) # here we decrypt a message we receive from the server
print(plaintext.decode())

sock.close()

print(f.decrypt(b"gAAAAABiaX46nQw0Nz4AFHLlRNTSSr9htfR8fYY85pF1OQUROT87z-4S6LHiIxDxOXMRWaoDbPVIPX4G3iuFVty2RfvHSiXKFaeDnYZh3aVH2VGRYvkN-Qo="))