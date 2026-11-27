"""
Python Networking Midterm - Part 1
TCP Socket Client

This program connects to a server, sends a message,
receives a response, and closes the connection.
"""

import socket
from datetime import datetime

# Server connection settings
HOST = "127.0.0.1"
PORT = 5000


def log_message(message):
    """Display a message with the current date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def start_client():
    """Connect to the server and exchange messages."""

    try:
        # Create a TCP socket using IPv4.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

            # Prevent indefinite waiting.
            client_socket.settimeout(10)

            # Connect to the server.
            log_message(f"Connecting to server at {HOST}:{PORT}...")
            client_socket.connect((HOST, PORT))

            log_message("Connected to server successfully.")

            # Send a message to the server.
            message = "Hello from the client!"
            client_socket.sendall((message + "\n").encode("utf-8"))

            log_message(f"Message sent: {message}")

            # Receive the server's response.
            with client_socket.makefile("rb") as reader:
                data = reader.readline(4097)

            if not data:
                log_message("Error: Server disconnected without responding.")
                return

            if len(data) > 4096 or not data.endswith(b"\n"):
                log_message("Error: Invalid or incomplete server response.")
                return

            # Decode and display the server's response.
            response = data.decode("utf-8").rstrip("\r\n")
            log_message(f"Response received: {response}")

            # Gracefully finish communication.
            client_socket.shutdown(socket.SHUT_WR)

            log_message("Disconnected from server successfully.")

    except ConnectionRefusedError:
        log_message("Error: Connection refused. Is the server running?")

    except TimeoutError:
        log_message("Error: Connection or communication timed out.")

    except UnicodeDecodeError:
        log_message("Error: Invalid response encoding.")

    except KeyboardInterrupt:
        log_message("Client stopped by the user.")

    except OSError as error:
        log_message(f"Socket error: {error}")

    finally:
        log_message("Client shutdown complete.")


# Run the client when this script is executed directly.
if __name__ == "__main__":
    start_client()
