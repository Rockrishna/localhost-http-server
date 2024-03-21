import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, address = server_socket.accept() # wait for client
    while True:
        data = client_socket.recv(1024)
        if data:
            break
    #data.decode() to grab data
    server_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())


    client_socket.close()
if __name__ == "__main__":
    main()
