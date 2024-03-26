import socket
import sys
import threading
import argparse
import os
import mimetypes

def handle_client(client_socket, directory):
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
        #print(path)
        if get.split(' ')[0] == 'GET':
            if path == '/' or 'echo' in path or 'user-agent' in path:
                if 'echo' in path:
                    path_parts = path.split('/')
                    echo = path_parts.index('echo')
                    string = '/'.join(path_parts[echo+1:])
                    client_socket.send(f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(string)}\r\n\r\n{string}'.encode())
                elif 'user-agent' in path:
                    header = user_agent.split(' ')[1]
                    client_socket.send(f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(header)}\r\n\r\n{header}'.encode())
                elif path[1:6] == 'files':
                    filename = path.split('/')[-1]
                    file_path = os.path.join(directory, filename)
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as f:
                            file_contents = f.read()
                        client_socket.send(f'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(file_contents)}\r\n\r\n'.encode() + file_contents)
                    else:
                        client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
                else:
                    client_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            else:
                client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        elif get.split(' ')[0] == 'POST':
            if 'files' in path:
                filename = path.split('/')[-1]
                file_path = os.path.join(directory, filename)
                if os.path.exists(file_path):
                    client_socket.send('HTTP/1.1 409 Conflict\r\n\r\n'.encode())
                else:
                    with open(file_path, 'wb') as f:
                        f.write(data.split(b'\r\n\r\n')[1])
                    client_socket.send('HTTP/1.1 201 Created\r\n\r\n'.encode())
            else:
                client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        else:
            client_socket.send('HTTP/1.1 405 Method Not Allowed\r\n\r\n'.encode())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, default=os.getcwd())
    args = parser.parse_args()

    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        while True:
            client_socket, address = server_socket.accept() # Wait for a client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, args.directory))
            client_thread.start()

if __name__ == "__main__":
    main()