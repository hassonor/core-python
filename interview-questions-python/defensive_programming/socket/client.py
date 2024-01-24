import socket

HOST = '127.0.0.1'  # The server's hostnames or IP address
PORT = 65432  # The port used by the server

# socket.AF_INET -> Ipv4 , socket.SOCK_STREAM -> TCP, s-> context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # The inner "()" represents a tuple
    s.sendall(b'Hello,world')
    data = s.recv(1024)
    
print('Received', repr(data))
