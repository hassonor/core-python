# Client - send tcp

# Usage: python3 client_send_file.py host port filename

import socket
import sys

if len(sys.argv) != 4:
    print(f"Usage: python3 {sys.argv[0]} host port filename")
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host, port))

data = True
with open(sys.argv[3], 'rb') as f:
    while data:
        data = f.read(4096)
        s.sendall(data)

s.close()
