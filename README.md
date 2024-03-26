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

To start the server, run the provided Python script with the desired directory as an argument. The server will then listen for incoming HTTP requests and respond according to the logic defined in the `handle_client` function.

## Contributing

Contributions to improve the server are welcome. Please feel free to fork this repository, make your changes, and submit a pull request.

