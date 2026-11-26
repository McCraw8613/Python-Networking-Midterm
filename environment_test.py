# Midterm Python environment verification

import sys
import platform
import socket
import time
from datetime import datetime

# Display environment information
print("=" * 55)
print("Python Networking Midterm - Environment Test")
print("=" * 55)

print("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Python Version:", sys.version)
print("Operating System:", platform.system())
print("Python Executable:", sys.executable)

# Test socket initialization
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM):
        print("Socket Module: SUCCESS")
except OSError as error:
    print("Socket Module: FAILED")
    print("Error:", error)
    sys.exit(1)

# Test the time module
print("Time Module: SUCCESS")
print("Current Unix Timestamp:", time.time())

print("=" * 55)
print("Midterm Environment Ready!")
print("=" * 55)