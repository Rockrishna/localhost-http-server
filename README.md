# Localhost HTTP Server

Welcome to the GitHub repository for our custom-built localhost HTTP server using Python. This server is designed to handle basic HTTP requests and serve files from a specified directory.

## Features

- **Simple HTTP GET requests handling**: The server can handle GET requests for paths including '/', 'echo', 'user-agent', and 'files'.
- **Echo functionality**: When the path includes 'echo', the server will respond with the text following the 'echo' in the path.
- **User-Agent Header Retrieval**: If 'user-agent' is included in the path, the server will respond with the User-Agent header value.
- **File Serving**: The 'files' path allows the server to serve files from the specified directory.

## How It Works

The server uses Python's `socket`, `sys`, `threading`, `argparse`, `os`, and `mimetypes` modules to set up a simple HTTP server. When a client connects, it receives data from the client, parses it, and sends an appropriate HTTP response.

## Usage

1. Run the script using the command: `python server.py`.
2. The server will handle incoming HTTP GET requests.
3. It can respond to the following paths:
   - `/echo/<text>`: Echoes the text sent in the request.
   - `/user-agent`: Returns the user-agent header from the request.
   - `/files/<filename>`: Serves the file specified if it exists in the server directory.

Make sure to replace `<text>` and `<filename>` with your actual text and file name.

## Contributing

Contributions to improve the server are welcome. Please feel free to fork this repository, make your changes, and submit a pull request.

