import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# socket.AF_INET -> Ipv4 , socket.SOCK_STREAM -> TCP, s-> context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started. Listening on {HOST}:{PORT}")

    try:
        # Accept new connection
        conn, address = s.accept()
        with conn:
            print("Connected by: ", address)
            while True:
                data = conn.recv(1024)
                if not data:
                    # No more data from client, the connection will be closed automatically by the 'with' statement
                    break

                # Decode received message
                text = data.decode('utf-8')
                print("Received Message: ", text)
                print("Enter message ")
                reply = input()
                replydata = bytearray(reply, "utf-8")
                newdata = bytearray(1024)

                for i in range(min(len(replydata), len(newdata))):
                    newdata[i] = replydata[i]

                conn.sendall(newdata)

    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    except socket.error as e:
        print(f"Socket error: {e}")
