# client side
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 8443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as s_sock:
        # communicate using sock, like an ordinary socket...
        pass


