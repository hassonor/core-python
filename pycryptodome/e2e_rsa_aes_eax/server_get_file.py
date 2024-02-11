# Server - receive tcp
# Usage: python3 server_get_file.py host port filename

import socket
import sys

if len(sys.argv) != 4:
    print(f"Usage: python3 {sys.argv[0]} host port filename")
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = sys.argv[1]
port = int(sys.argv[2])
s.bind((host, port))
s.listen()

conn, addr = s.accept()
data = True
with open(sys.argv[3], 'wb') as f:
    while data:
        data = conn.recv(4096)
        f.write(data)
conn.close()
