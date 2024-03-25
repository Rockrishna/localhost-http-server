import socket

def main():
    data = False
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        while True:
            client_socket, address = server_socket.accept() # Wait for a client
            if client_socket:
                with client_socket:
                    while True:
                        data = client_socket.recv(1024)
                        if data:
                            break
                if data:
                    break
                # Send HTTP response to the client
                #client_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        parsed_data = data.decode()
        #parse the data
        get, host, user_agent = parsed_data.split('\r\n')[0], parsed_data.split('\r\n')[1], parsed_data.split('\r\n')[2]
        if get[4] == r'/':
            client_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        else:
            client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())

    client_socket.close()
if __name__ == "__main__":
    main()