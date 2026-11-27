# Python Networking Midterm

## Project Overview

This project was developed for a Security Automation course to demonstrate Python networking fundamentals, TCP socket
communication, port scanning, error handling, and responsible security automation.

The project consists of two primary programming assignments:

- Part 1: TCP Socket Client and Server
- Part 2: TCP Port Scanner

Both assignments were developed and tested using Python 3.12, PyCharm, Miniconda, and Windows 11.

## Project Objectives

- Establish a TCP connection between a client and server.
- Demonstrate bidirectional message exchange.
- Implement proper socket initialization and connection handling.
- Demonstrate graceful connection termination.
- Develop a TCP port scanner for authorized targets.
- Identify open and closed ports.
- Handle connection timeouts and network errors.
- Validate user input and restrict unauthorized scanning.
- Implement delays and scan limits to support responsible scanning.
- Evaluate scanner performance across different port ranges.
- Document successful and unsuccessful test executions.
- Demonstrate version control using Git and GitHub.

## Educational Purpose

This project is intended for educational purposes only. All network scanning is restricted to authorized targets. The
programs demonstrate foundational networking concepts and their application to cybersecurity and security automation.

## Project Structure

The project is organized as follows:

```text
Python-Networking-Midterm/
├── environment_test.py
├── socket_server.py
├── socket_client.py
├── port_scanner.py
├── test_port_scanner.py
├── README.md
├── .gitignore
└── screenshots/
```

### File Descriptions

| File                   | Description                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `environment_test.py`  | Verifies the Python development environment and required modules.                                                          |
| `socket_server.py`     | Implements a TCP server that listens for client connections and exchanges messages.                                        |
| `socket_client.py`     | Implements a TCP client that connects to the server and exchanges messages.                                                |
| `port_scanner.py`      | Implements an authorized TCP port scanner with input validation, error handling, timestamps, and performance measurements. |
| `test_port_scanner.py` | Provides an automated unit test that simulates an unreachable host without making actual network connections.              |
| `README.md`            | Provides project documentation, setup instructions, usage instructions, and testing results.                               |
| `.gitignore`           | Prevents unnecessary local files and directories from being uploaded to GitHub.                                            |
| `screenshots/`         | Stores local screenshots documenting successful and unsuccessful test executions.                                          |

The screenshots directory is excluded from Git version control. Screenshots are maintained locally for separate
assignment submission.

## System Requirements and Dependencies

### Development Environment

| Component                          | Version or Description     |
|------------------------------------|----------------------------|
| Operating System                   | Windows 11                 |
| Python                             | 3.12.16                    |
| Integrated Development Environment | PyCharm                    |
| Environment Manager                | Miniconda                  |
| Conda Environment                  | security-automation        |
| Version Control                    | Git                        |
| Repository Hosting                 | GitHub                     |
| AI Development Assistance          | ChatGPT and GitHub Copilot |

### Python Standard Library Modules

| Module          | Purpose                                                             |
|-----------------|---------------------------------------------------------------------|
| `socket`        | Establishes TCP connections and performs port scanning.             |
| `datetime`      | Generates timestamps for program activity and test results.         |
| `time`          | Implements scan delays and measures execution performance.          |
| `unittest`      | Provides automated unit testing capabilities.                       |
| `unittest.mock` | Simulates network errors without making actual network connections. |

### External Dependencies

The networking programs and automated unit test use Python standard library modules. No additional third-party Python
packages are required.

An internet connection is required when scanning the authorized external target, scanme.nmap.org, or accessing GitHub.

Localhost testing does not require an internet connection.

## Installation and Environment Setup

### Step 1: Install Required Software

Install the following development tools if they are not already available:

- Miniconda
- PyCharm
- Git

A GitHub account is useful for repository management but is not required to execute the Python programs.

### Step 2: Clone the GitHub Repository

Open a terminal and execute the following commands:

```bash
git clone https://github.com/McCraw8613/Python-Networking-Midterm.git
cd Python-Networking-Midterm
```

### Step 3: Create the Conda Environment

Open the Miniconda Prompt and execute:

```bash
conda create --name security-automation python=3.12
```

If the environment already exists, skip the creation command.

### Step 4: Activate the Conda Environment

```bash
conda activate security-automation
```

### Step 5: Verify the Python Installation

```bash
python --version
```

This project was developed and tested using Python 3.12.16.

### Step 6: Configure PyCharm

1. Open PyCharm.
2. Open the cloned Python-Networking-Midterm project.
3. Navigate to Settings and locate the Python Interpreter settings.
4. Select the existing Conda environment named security-automation.
5. Apply and save the interpreter configuration.

### Step 7: Verify the Development Environment

Run the environment verification script:

```bash
python environment_test.py
```

Confirm that the Python interpreter and required networking modules are available.

No additional third-party Python packages are required to run the networking programs or the automated unit test.

## Part 1: TCP Socket Client and Server

### Overview

The TCP socket client and server demonstrate reliable network communication between two Python programs running on the
same computer.

### Connection Configuration

| Setting        | Value         |
|----------------|---------------|
| Protocol       | TCP           |
| Address Family | IPv4          |
| Host Address   | 127.0.0.1     |
| Port           | 5000          |
| Communication  | Bidirectional |
| Network Scope  | Localhost     |

### Step 1: Start the Server

Open a terminal in the project directory with the Conda environment activated and execute:

```bash
python socket_server.py
```

The server initializes a TCP socket, binds to localhost, listens on port 5000, and waits for a client connection.

Alternatively, right-click socket_server.py in PyCharm and select Run.

### Step 2: Start the Client

Keep the server running.

Open a separate terminal with the Conda environment activated and execute:

```bash
python socket_client.py
```

Alternatively, right-click socket_client.py in PyCharm and select Run.

The client attempts to establish a TCP connection with the server at 127.0.0.1 on port 5000.

### Step 3: Exchange Messages

Follow the client program's prompts to send a message to the server.

Verify that:

- The client successfully connects to the server.
- The server receives the client's message.
- The server sends a response.
- The client receives the server's response.
- Program activity is recorded with timestamps.

### Step 4: Disconnect

Follow the program's termination procedure to close the client connection.

Verify that the connection terminates gracefully and socket resources are released.

### Step 5: Test Connection Error Handling

Ensure that the server is no longer running.

Execute the client again:

```bash
python socket_client.py
```

The client should handle the unsuccessful connection attempt and display an appropriate error message without an
unhandled exception.

### Step 6: Test Server Port Conflict

Start the server and attempt to launch a second server instance using the same host address and port.

The second server instance should handle the address or port conflict appropriately.

Stop any remaining server instances after testing.

### Part 1 Features

- TCP socket initialization.
- Server binding and listening.
- Client connection establishment.
- Bidirectional message exchange.
- Exception handling.
- Connection refusal handling.
- Server port conflict handling.
- Graceful connection termination.
- Timestamped activity messages.
- Documented Python source code.

## Part 2: TCP Port Scanner

### Overview

The TCP port scanner identifies open and closed TCP ports on authorized targets. It supports common port scanning,
custom port ranges, and individually selected ports.

The scanner includes input validation, connection timeouts, network error handling, timestamps, and performance
measurements.

### Scanner Configuration

| Setting                         | Value                      |
|---------------------------------|----------------------------|
| Protocol                        | TCP                        |
| Address Family                  | IPv4                       |
| Connection Timeout              | 3.0 seconds                |
| Scan Delay                      | 0.5 seconds                |
| Minimum Port                    | 1                          |
| Maximum Port                    | 65535                      |
| Maximum Local Ports per Scan    | 100                        |
| Maximum External Ports per Scan | 10                         |
| Scanning Method                 | Sequential TCP connections |

### Authorized Targets

Scanning is restricted to the following targets:

- localhost
- 127.0.0.1
- scanme.nmap.org

All other targets are rejected by the program.

### Step 1: Start the Port Scanner

Open a terminal in the project directory with the Conda environment activated and execute:

```bash
python port_scanner.py
```

Alternatively, right-click port_scanner.py in PyCharm and select Run.

### Step 2: Select an Authorized Target

Enter an authorized hostname or IP address when prompted.

### Step 3: Select a Scanning Option

| Option | Description              |
|--------|--------------------------|
| 1      | Scan common ports        |
| 2      | Scan a custom port range |
| 3      | Scan specific ports      |
| 4      | Exit the program         |

### Step 4: Scan Common Ports

Enter localhost as the target and select option 1.

The scanner attempts TCP connections to the following ports:

| Port | Common Service |
|------|----------------|
| 21   | FTP            |
| 22   | SSH            |
| 80   | HTTP           |
| 443  | HTTPS          |

These service names represent conventional port assignments. An open port does not confirm which service is running.

### Step 5: Scan a Custom Port Range

Start socket_server.py and keep the server running.

Launch port_scanner.py separately and enter:

```text
Target: 127.0.0.1
Menu option: 2
Starting port: 4998
Ending port: 5002
```

Port 5000 should be detected as open while the server is listening.

Restart the server if necessary because the scanner's connection may cause the server to terminate.

### Step 6: Scan Specific Ports

Select option 3 and enter the desired port numbers separated by commas.

The authorized external target used during testing was scanme.nmap.org, with ports 22, 80, and 443 selected.

External scanning must remain limited and non-aggressive.

### Step 7: Interpret Scan Results

| Result      | Meaning                                           |
|-------------|---------------------------------------------------|
| OPEN        | A TCP connection was successfully established.    |
| CLOSED      | The connection was explicitly refused.            |
| TIMEOUT     | The connection attempt exceeded the waiting time. |
| UNREACHABLE | A network or host unreachable error occurred.     |
| ERROR       | An error prevented the connection attempt.        |
| UNKNOWN     | An unclassified socket error occurred.            |

A timeout does not necessarily indicate that a port is closed.

### Step 8: Run the Automated Unit Test

Execute the following command:

```bash
python -m unittest -v test_port_scanner
```

Alternatively, run test_port_scanner.py using PyCharm's unit testing interface.

The unit test simulates Windows socket error 10065 to verify unreachable-host error handling.

No actual network connections are made during this test.

### Part 2 Features

- Common port scanning.
- Custom port range scanning.
- Individual port selection.
- Authorized target validation.
- Port number validation.
- Sequential TCP connection attempts.
- Connection timeout handling.
- Connection refusal handling.
- Hostname resolution error handling.
- Unreachable-host error handling.
- Scan delays and scan size restrictions.
- Timestamped scan results.
- Scan duration measurements.
- Automated unit testing.
- Graceful program termination.

## Testing and Verification Results

Testing was conducted on November 27, 2026, using Windows 11, PyCharm, and Python 3.12.16.

Both successful and unsuccessful execution scenarios were evaluated to verify program functionality, error handling, and
security restrictions.

### Part 1: TCP Socket Client and Server Testing

| Test Case                   | Expected Result                          | Test Status |
|-----------------------------|------------------------------------------|-------------|
| Server initialization       | Server binds and listens for connections | Passed      |
| Client connection           | Client establishes a TCP connection      | Passed      |
| Client message transmission | Server receives the client message       | Passed      |
| Server response             | Client receives the server response      | Passed      |
| Graceful disconnection      | Socket resources are released            | Passed      |
| Server unavailable          | Client handles connection refusal        | Passed      |
| Server port conflict        | Server handles an address conflict       | Passed      |

### Part 2: TCP Port Scanner Testing

| Test Case              | Expected Result                                      | Test Status                       |
|------------------------|------------------------------------------------------|-----------------------------------|
| Common port scan       | Scan ports 21, 22, 80, and 443                       | Executed                          |
| Custom localhost range | Scan the selected port range                         | Passed                            |
| Open port detection    | Identify a listening TCP service                     | Passed if confirmed by screenshot |
| Closed port detection  | Identify a refused connection                        | Passed                            |
| External target scan   | Attempt connections to an authorized external target | Attempted                         |
| Invalid port numbers   | Reject ports outside the valid range                 | Passed                            |
| Unauthorized target    | Reject a target outside the authorized list          | Passed                            |
| Unreachable host       | Correctly classify simulated socket error 10065      | Passed                            |
| Performance testing    | Measure execution time across different ranges       | Passed                            |
| Program termination    | Exit without an unhandled exception                  | Passed                            |

### Troubleshooting and Corrective Actions

During initial testing, the port scanner encountered Windows socket error 10035 and connection timeout results.

Additional testing and adjustments were performed to improve socket error handling and result classification.

The connection timeout was increased to 3.0 seconds.

Subsequent localhost testing successfully identified closed ports instead of prematurely reporting timeouts.

### Verified Test Results

| Test                           | Timestamp           | Observed Result              |
|--------------------------------|---------------------|------------------------------|
| Invalid port range             | 2026-11-27 12:45:11 | Invalid port rejected        |
| External hostname resolution   | 2026-11-27 12:49:30 | Hostname resolution failed   |
| Unauthorized target            | 2026-11-27 12:56:36 | Unauthorized target rejected |
| Closed port 5000               | 2026-11-27 12:59:23 | CLOSED                       |
| Simulated unreachable host     | 2026-11-27 13:03:02 | UNREACHABLE                  |
| Five-port performance retest   | 2026-11-27 13:06:15 | Five closed ports            |
| Ten-port performance retest    | 2026-11-27 13:08:15 | Ten closed ports             |
| Twenty-port performance retest | 2026-11-27 13:10:02 | Twenty closed ports          |

All timestamps represent local system time.

### External Target Testing Limitation

During an authorized scan of scanme.nmap.org, the scanner encountered a hostname resolution error.

The program handled the error without crashing and completed its shutdown process successfully.

The hostname resolution failure prevented verification of the external target's port status during that attempt.

### Automated Unreachable-Host Testing

The automated unit test uses Python's unittest and unittest.mock modules to simulate Windows socket error 10065.

Expected result: UNREACHABLE

Actual result: UNREACHABLE

Tests executed: 1

Tests passed: 1

Execution duration: 0.509 seconds

Process exit code: 0

No actual network connections were made during the automated test.

### Screenshot Evidence

Screenshots were captured throughout development and testing to document:

- Environment verification.
- GitHub repository configuration.
- GitHub Copilot verification.
- Successful client-server communication.
- Server port conflicts.
- Connection refusal handling.
- Common and custom port scanning.
- Open and closed port detection testing.
- Invalid input handling.
- Unauthorized target rejection.
- External hostname resolution errors.
- Automated unit testing.
- Performance measurements.
- Successful GitHub uploads.

Screenshot evidence is maintained locally for separate assignment submission.

## Performance Analysis

Performance testing was conducted on November 27, 2026, to evaluate how the TCP port scanner's execution time changes as
the number of selected ports increases.

### Testing Configuration

| Parameter                       | Configuration              |
|---------------------------------|----------------------------|
| Target                          | 127.0.0.1                  |
| Operating system                | Windows 11                 |
| Python version                  | 3.12.16                    |
| Scan method                     | Sequential TCP connections |
| Connection timeout              | 3.0 seconds                |
| Scan delay                      | 0.5 seconds                |
| Maximum ports per local scan    | 100                        |
| Maximum ports per external scan | 10                         |

### Final Performance Results

| Port Range | Ports Scanned | Open | Closed | Other | Duration      |
|------------|---------------|------|--------|-------|---------------|
| 6000-6004  | 5             | 0    | 5      | 0     | 12.66 seconds |
| 6000-6009  | 10            | 0    | 10     | 0     | 25.41 seconds |
| 6000-6019  | 20            | 0    | 20     | 0     | 50.77 seconds |

### Average Execution Time per Port

| Ports Scanned | Total Duration | Average Time per Port |
|---------------|----------------|-----------------------|
| 5             | 12.66 seconds  | 2.53 seconds          |
| 10            | 25.41 seconds  | 2.54 seconds          |
| 20            | 50.77 seconds  | 2.54 seconds          |

### Performance Test Timestamps

| Test             | Start Time | Completion Time |
|------------------|------------|-----------------|
| Five-port scan   | 13:06:03   | 13:06:15        |
| Ten-port scan    | 13:07:49   | 13:08:15        |
| Twenty-port scan | 13:09:11   | 13:10:02        |

All tests were conducted on November 27, 2026. Timestamps represent local system time.

### Performance Observations

The final performance tests demonstrated approximately linear execution-time scaling.

Doubling the number of selected ports approximately doubled the total scan duration.

The scanner maintained a consistent average execution time of approximately 2.54 seconds per port during the final
localhost performance tests.

All 35 connection attempts across the three final performance tests were classified as CLOSED.

### Initial and Final Performance Comparison

| Ports Scanned | Initial Duration | Final Duration |
|---------------|------------------|----------------|
| 5             | 7.55 seconds     | 12.66 seconds  |
| 10            | 15.13 seconds    | 25.41 seconds  |
| 20            | 30.18 seconds    | 50.77 seconds  |

The initial performance tests returned TIMEOUT results.

After increasing the connection timeout to 3.0 seconds, the repeated tests successfully identified closed ports.

Although the final tests required additional execution time, the longer timeout allowed the scanner to receive
connection refusal responses rather than prematurely classifying the connection attempts as timeouts.

### Security and Performance Trade-Offs

The scanner intentionally performs connection attempts sequentially and includes a delay between attempts.

This design reduces the rate of connection attempts and supports responsible network scanning practices.

The scanner prioritizes responsible operation, controlled resource usage, and meaningful result classification over
maximum scanning speed.

### Performance Limitations

Execution times may vary depending on network conditions, operating system behavior, firewall configuration, service
availability, and connection timeout settings.

The recorded results represent the specific localhost test environment and selected port ranges.

No aggressive scanning or large-scale external performance testing was conducted.

## Security and Ethical Considerations

Network programming and port scanning are important components of cybersecurity and security automation.

However, these technologies must be used responsibly, ethically, and within authorized boundaries.

### Authorized Scanning Targets

The port scanner restricts scanning to the following authorized targets:

| Target          | Purpose                               |
|-----------------|---------------------------------------|
| localhost       | Local development and testing         |
| 127.0.0.1       | Local loopback testing                |
| scanme.nmap.org | Authorized external scanning practice |

Targets outside the authorized list are rejected before scanning begins.

This restriction reduces the risk of accidentally scanning unauthorized systems.

### Implemented Security Controls

The following security controls were incorporated into the port scanner:

- Authorized target validation.
- TCP port number validation.
- Sequential connection attempts.
- A 0.5-second delay between connection attempts.
- A 3.0-second connection timeout.
- A maximum of 100 ports per local scan.
- A maximum of 10 ports per external scan.
- Network exception handling.
- Socket resource management.
- Timestamped activity messages.
- Graceful program termination.

These controls support responsible scanning and reduce unnecessary network activity.

### Client and Server Security

The TCP client and server use the local loopback address, 127.0.0.1, for communication.

This configuration restricts the intended communication to the local computer.

The programs also demonstrate:

- Connection error handling.
- Server port conflict handling.
- Proper socket resource management.
- Graceful connection termination.
- Timestamped activity reporting.

The client and server are educational demonstrations and are not intended for production deployment.

The communication does not implement encryption or authentication.

Sensitive or confidential information should not be transmitted using these demonstration programs.

### Legal Considerations

Network scanning should only be performed against systems for which appropriate authorization has been obtained.

Unauthorized scanning may violate organizational policies, acceptable use agreements, or applicable laws, depending on
the circumstances.

Public accessibility does not automatically constitute permission to scan a system.

Users are responsible for obtaining authorization and complying with applicable requirements.

### Ethical Considerations

Responsible cybersecurity practices include:

- Obtaining authorization before scanning.
- Respecting the scope of authorized testing.
- Avoiding unnecessary network traffic.
- Protecting confidential information.
- Accurately reporting testing results.
- Respecting system availability.
- Avoiding exploitation of discovered services.
- Documenting limitations and unsuccessful tests.

The port scanner identifies TCP connection results and does not attempt to exploit discovered services.

An open port does not automatically indicate that a system contains a security vulnerability.

### Safe Error-Handling Testing

The unreachable-host unit test uses a simulated Windows socket error to verify exception handling.

This approach allows the program's error-handling capabilities to be evaluated without attempting connections to
unauthorized systems.

No actual network connections are made during the automated unreachable-host test.

### Repository Security

The Git repository excludes unnecessary local development files and screenshot evidence through the .gitignore
configuration.

Sensitive information, passwords, authentication tokens, and private credentials should never be committed to a public
GitHub repository.

### Educational Use Disclaimer

This project was developed for educational purposes as part of a Security Automation course.

The programs are intended to demonstrate foundational Python networking, TCP socket communication, error handling, and
responsible port scanning.

The software is not intended for unauthorized network reconnaissance, exploitation, or disruption.

### Security and Ethical Resources

Nmap Project. (n.d.). ScanMe!
https://scanme.nmap.org/

National Institute of Standards and Technology. (2008). Technical guide to information security testing and assessment
(Special Publication 800-115).
https://doi.org/10.6028/NIST.SP.800-115

## AI Assistance Disclosure

Artificial intelligence tools were used during the development of this project in accordance with the course's permitted
use of AI-assisted programming.

### AI Tools Used

| Tool           | Purpose                                                                            |
|----------------|------------------------------------------------------------------------------------|
| ChatGPT        | Programming guidance, code generation, troubleshooting, testing, and documentation |
| GitHub Copilot | Python networking explanations and development assistance                          |

### ChatGPT Assistance

ChatGPT provided assistance throughout the project, including:

- Project planning and organization.
- PyCharm project configuration.
- Python development environment verification.
- Git and GitHub repository configuration.
- TCP socket server development.
- TCP socket client development.
- TCP port scanner development.
- Python code explanations.
- Windows socket error troubleshooting.
- Network exception handling.
- Input validation.
- Authorized target restrictions.
- Connection timeout adjustments.
- Automated unit test development.
- Performance testing guidance.
- Screenshot documentation guidance.
- README documentation development.

AI-generated code and recommendations were implemented and tested in the local development environment.

### GitHub Copilot Assistance

GitHub Copilot was used to support the understanding of Python networking concepts within PyCharm.

An initial verification prompt was:

> Explain how Python's socket module establishes a
> TCP connection between a client and a server on
> localhost. Explain the process in beginner-friendly
> terms without generating code.

The purpose of this prompt was to verify GitHub Copilot functionality and establish a foundational understanding of TCP
socket communication before program development.

### Implementation and Verification

Project implementation and verification activities performed by the student included:

- Configuring the development environment.
- Creating and organizing project files.
- Implementing AI-assisted source code.
- Executing Python programs.
- Conducting successful and unsuccessful tests.
- Applying troubleshooting recommendations.
- Adjusting connection timeout settings.
- Repeating tests after corrective changes.
- Capturing timestamped screenshot evidence.
- Recording actual performance measurements.
- Managing Git and GitHub operations.

### Examples of Corrective Changes

During development and testing, corrective changes included:

- Addressing Windows socket error 10035.
- Improving network exception classification.
- Increasing the connection timeout to 3.0 seconds.
- Distinguishing connection refusals from timeouts.
- Testing unreachable-host error handling using a simulated socket exception.

These changes were supported by AI-assisted troubleshooting and evaluated through program execution and testing.

### AI Limitations and Verification

AI-generated recommendations may contain errors, incorrect assumptions, or incomplete information.

Recommendations were evaluated through practical testing in the Windows 11 development environment.

Actual program output, timestamps, screenshots, and measured execution durations were used as evidence of testing
results.

Unsuccessful tests and identified limitations were documented rather than represented as successful executions.

### Academic Integrity

AI assistance was used for programming, technical explanations, troubleshooting, testing guidance, and project
documentation.

The student's personal reflection is a separate assignment component and must be completed independently in accordance
with the course's academic integrity requirements.

This disclosure summarizes the use of AI tools during project development.