import socket

def main():
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:

            while True:

                client_socket, address = server_socket.accept() # Wait for a client

                with client_socket:

                    while True:

                        data = client_socket.recv(1024)

                        if data:

                            break

                    # Send HTTP response to the client

                    client_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

    client_socket.close()
if __name__ == "__main__":
    main()
