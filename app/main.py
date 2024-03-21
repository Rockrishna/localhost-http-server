import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, address = server_socket.accept() # wait for client
    data = client_socket.recv(1024)
    print(data.decode())

if __name__ == "__main__":
    main()
