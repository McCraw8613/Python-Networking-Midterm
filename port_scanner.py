"""
Python Networking Midterm - Part 2
TCP Port Scanner

Purpose:
    Identify open and closed TCP ports on authorized targets.

Security:
    Only authorized targets may be scanned.
    Scanning is performed sequentially with a delay
    between connection attempts.
"""

import socket
import time
from datetime import datetime


# Authorized targets for this assignment.
AUTHORIZED_TARGETS = (
    "localhost",
    "127.0.0.1",
    "scanme.nmap.org",
)

# Common TCP ports used for testing.
COMMON_PORTS = (21, 22, 80, 443)

# Maximum time to wait for a connection.
TIMEOUT = 3.0

# Delay between connection attempts in seconds.
SCAN_DELAY = 0.5

# Valid TCP port boundaries.
MIN_PORT = 1
MAX_PORT = 65535

# Limit the number of ports per scan.
MAX_PORTS_PER_SCAN = 100

# Smaller limit for the authorized external target.
MAX_EXTERNAL_PORTS = 10

def log_message(message):
    """Display a message with the current date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def validate_target(target):
    """Verify that the target is authorized for scanning."""
    target = target.strip().lower()

    if target not in AUTHORIZED_TARGETS:
        raise ValueError(
            "Unauthorized target. Only localhost, "
            "127.0.0.1, and scanme.nmap.org are permitted."
        )

    return target


def validate_port(port):
    """Verify that a port is an integer within the valid range."""
    try:
        port = int(port)
    except ValueError:
        raise ValueError("Port numbers must be integers.")

    if not MIN_PORT <= port <= MAX_PORT:
        raise ValueError("Port numbers must be between 1 and 65535.")

    return port


def validate_port_range(start_port, end_port, target):
    """Validate the port range and enforce scanning limits."""
    target = validate_target(target)
    start_port = validate_port(start_port)
    end_port = validate_port(end_port)

    if start_port > end_port:
        raise ValueError(
            "The starting port cannot exceed the ending port."
        )

    total_ports = end_port - start_port + 1

    if target == "scanme.nmap.org":
        limit = MAX_EXTERNAL_PORTS
    else:
        limit = MAX_PORTS_PER_SCAN

    if total_ports > limit:
        raise ValueError(
            f"Scan limit exceeded. Maximum allowed: {limit} ports."
        )

    return list(range(start_port, end_port + 1))

def scan_port(target, port):
    """Attempt a TCP connection to an authorized target."""

    target = validate_target(target)
    port = validate_port(port)

    try:
        # Create an IPv4 TCP socket.
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as scanner_socket:

            # Limit the connection waiting time.
            scanner_socket.settimeout(TIMEOUT)

            # Attempt a TCP connection.
            scanner_socket.connect((target, port))

            return "OPEN"

    except ConnectionRefusedError:
        return "CLOSED"

    except socket.gaierror:
        return "ERROR: Hostname resolution failed"

    except TimeoutError:
        return "TIMEOUT"

    except OSError as error:
        if error.errno in (10051, 10065, 101, 113):
            return "UNREACHABLE"

        return f"ERROR: {error}"

    finally:
        # Pause between connection attempts.
        time.sleep(SCAN_DELAY)


def display_summary(target, results, elapsed_time):
    """Display the completed scan results."""

    open_ports = [
        port for port, status in results.items()
        if status == "OPEN"
    ]

    closed_ports = [
        port for port, status in results.items()
        if status == "CLOSED"
    ]

    other_ports = (
        len(results) - len(open_ports) - len(closed_ports)
    )

    print("\n" + "=" * 50)
    print("PORT SCAN SUMMARY")
    print("=" * 50)

    log_message(f"Target: {target}")
    log_message(f"Total ports scanned: {len(results)}")
    log_message(f"Open ports: {len(open_ports)}")
    log_message(f"Closed ports: {len(closed_ports)}")
    log_message(f"Other results: {other_ports}")

    if open_ports:
        log_message(f"Open port numbers: {open_ports}")
    else:
        log_message("No open ports detected.")

    log_message(f"Scan duration: {elapsed_time:.2f} seconds")
    log_message("Scan completed.")

    print("=" * 50)


def execute_scan(target, ports):
    """Execute a sequential scan of authorized ports."""

    target = validate_target(target)

    # Validate and remove duplicate port numbers.
    ports = list(dict.fromkeys(
        validate_port(port) for port in ports
    ))

    if not ports:
        raise ValueError("No ports were selected.")

    # Enforce the appropriate scan limit.
    if target == "scanme.nmap.org":
        limit = MAX_EXTERNAL_PORTS
    else:
        limit = MAX_PORTS_PER_SCAN

    if len(ports) > limit:
        raise ValueError(
            f"Scan limit exceeded. Maximum: {limit} ports."
        )

    results = {}

    print("\n" + "=" * 50)
    log_message("Starting TCP port scan.")
    log_message(f"Target: {target}")
    log_message(f"Ports selected: {len(ports)}")
    print("=" * 50)

    # Record the starting time.
    start_time = time.perf_counter()

    # Scan each selected port individually.
    for port in ports:
        status = scan_port(target, port)
        results[port] = status

        log_message(f"Port {port}: {status}")

    # Calculate the total scan duration.
    elapsed_time = time.perf_counter() - start_time

    display_summary(target, results, elapsed_time)

def main():
    """Collect user input and start the port scanner."""

    print("=" * 50)
    print("PYTHON TCP PORT SCANNER")
    print("=" * 50)

    log_message("Port scanner started.")

    print("\nAuthorized targets:")

    for target in AUTHORIZED_TARGETS:
        print(f"  - {target}")

    try:
        # Collect and validate the target.
        target = input("\nEnter target: ")
        target = validate_target(target)

        # Display available scanning options.
        print("\nSCAN OPTIONS")
        print("1. Scan common ports")
        print("2. Scan a custom port range")
        print("3. Scan specific ports")
        print("4. Exit program")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            ports = list(COMMON_PORTS)

        elif choice == "2":
            start_port = input("Enter starting port: ")
            end_port = input("Enter ending port: ")

            ports = validate_port_range(
                start_port, end_port, target
            )

        elif choice == "3":
            port_input = input(
                "Enter port numbers separated by commas: "
            )

            ports = [
                validate_port(port.strip())
                for port in port_input.split(",")
            ]

        elif choice == "4":
            log_message("Exit selected by user.")
            return

        else:
            raise ValueError(
                "Invalid menu choice. Select 1, 2, 3, or 4."
            )

        # Execute the selected scan.
        execute_scan(target, ports)

    except ValueError as error:
        log_message(f"Input error: {error}")

    except KeyboardInterrupt:
        log_message("Scan cancelled by the user.")

    except EOFError:
        log_message("Input ended unexpectedly.")

    except OSError as error:
        log_message(f"Network error: {error}")

    finally:
        log_message("Port scanner shutdown complete.")


# Run the scanner when this script is executed directly.
if __name__ == "__main__":
    main()
