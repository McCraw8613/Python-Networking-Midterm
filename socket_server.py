"""
Python Networking Midterm - Part 1
TCP Socket Server

This program listens for a client connection, receives
a message, sends a response, and closes the connection.
"""

import socket
from datetime import datetime

# Server configuration
HOST = "127.0.0.1"
PORT = 5000


def log_message(message):
    """Display a message with the current date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def start_server():
    """Start the TCP server and handle a client connection."""

    try:
        # Create a TCP socket using IPv4.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

            # Assign the IP address and port to the server.
            server_socket.bind((HOST, PORT))

            # Listen for incoming client connections.
            server_socket.listen(1)

            log_message("Server started successfully.")
            log_message(f"Server listening on {HOST}:{PORT}")
            log_message("Waiting for a client connection...")

            # Accept an incoming client connection.
            connection, address = server_socket.accept()

            with connection:
                log_message(f"Client connected from {address}")

                # Set a timeout to prevent indefinite waiting for data.
                connection.settimeout(30)

                # Read one newline-terminated message from the client.
                with connection.makefile("rb") as reader:
                    data = reader.readline(4097)

                if not data:
                    log_message("Client disconnected without sending a message.")
                    return

                if len(data) > 4096 or not data.endswith(b"\n"):
                    log_message("Invalid or incomplete client message.")
                    return

                # Decode and display the received message.
                message = data.decode("utf-8").rstrip("\r\n")
                log_message(f"Message received: {message}")

                # Send a response to the client.
                response = "Hello from the server! Message received."
                connection.sendall((response + "\n").encode("utf-8"))

                log_message(f"Response sent: {response}")

                # Signal that communication is finished.
                connection.shutdown(socket.SHUT_WR)

            log_message("Client connection closed successfully.")

    except KeyboardInterrupt:
        log_message("Server stopped by the user.")

    except TimeoutError:
        log_message("Error: Client communication timed out.")

    except UnicodeDecodeError:
        log_message("Error: Invalid message encoding.")

    except OSError as error:
        log_message(f"Socket error: {error}")

    finally:
        log_message("Server shutdown complete.")


# Run the server when this script is executed directly.
if __name__ == "__main__":
    start_server()