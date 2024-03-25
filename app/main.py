import socket
import sys

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
                parsed_data = data.decode()
                #parse the data
                print(parsed_data)
                get, host, user_agent = parsed_data.split('\r\n')[0], parsed_data.split('\r\n')[1], parsed_data.split('\r\n')[2]
                path = get.split(' ')[1]
                if r"/" == path:
                    client_socket.send(f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n{string}'.encode())
                else:
                    client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
                client_socket.close()
                break

if __name__ == "__main__":
    main()