Overview
This project is a Python-based network port scanner designed to identify open TCP ports on a specified host. It establishes socket connections to target ports and reports their availability, enabling efficient network reconnaissance and basic security assessment.
Features
Scans a configurable range of TCP ports on a target host
Identifies and reports open ports in real time
Handles connection timeouts to ensure efficient scanning
Provides clear and structured output for analysis
How It Works
The scanner iterates through a defined port range and attempts to establish TCP connections using Python’s socket library. If a connection is successful, the port is marked as open. Closed or filtered ports are skipped based on connection behavior and timeout responses.
Technologies Used
Python
TCP/IP Networking
Socket Programming
Use Cases
Network surface mapping
Identifying exposed services
Learning and understanding TCP/IP behavior
Basic security reconnaissance
Usage
Specify the target host (IP address or domain).
Define the range of ports to scan.
Run the script to receive a list of open ports on the target system.
