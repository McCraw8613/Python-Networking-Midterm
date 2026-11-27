"""
Port Scanner Error Handling Test

Purpose:
    Verify that the port scanner correctly handles
    an unreachable-host error using a simulated
    network failure.

Security:
    No actual network connections are made.
"""

import unittest
from unittest.mock import patch
from datetime import datetime

from port_scanner import scan_port


class TestPortScanner(unittest.TestCase):
    """Test the port scanner's error-handling behavior."""

    @patch("port_scanner.socket.socket")
    def test_unreachable_host(self, mock_socket):
        """Simulate an unreachable-host error."""

        # Display the test timestamp.
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(f"\n[{timestamp}] Starting unreachable-host test.")

        # Access the simulated socket connection.
        simulated_socket = (
            mock_socket.return_value.__enter__.return_value
        )

        # Simulate Windows error 10065: Host unreachable.
        simulated_socket.connect.side_effect = OSError(
            10065, "No route to host"
        )

        # Execute the scanner using an authorized target.
        result = scan_port("127.0.0.1", 80)

        print("Target: 127.0.0.1")
        print("Port: 80")
        print("Simulated error: 10065")
        print("Expected result: UNREACHABLE")
        print(f"Actual result: {result}")

        # Verify that the scanner returns the correct result.
        self.assertEqual(result, "UNREACHABLE")

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(f"[{timestamp}] Unreachable-host test passed.")
        print("No actual network connections were made.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
