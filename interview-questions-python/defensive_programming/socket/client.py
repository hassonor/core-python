import socket

HOST = '127.0.0.1'  # The server's hostnames or IP address
PORT = 65432  # The port used by the server

# socket.AF_INET -> Ipv4 , socket.SOCK_STREAM -> TCP, s-> context manager
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # The inner "()" represents a tuple
        s.sendall(b'Hello, world')  # Send a message
        data = s.recv(1024)  # Receive a response

        print('Received', repr(data))
except ConnectionRefusedError:
    print(f"Connection failed. Is the server running on {HOST}:{PORT}?")
except socket.error as e:
    print(f"Socket error: {e}")
