## Overview
This project is a Python-based TCP port scanner designed to identify open ports on a specified host. It demonstrates efficient network reconnaissance techniques and practical understanding of TCP/IP protocols.

## Features
- Scan a configurable range of TCP ports on a target host  
- Identify open ports and report them in real-time  
- Efficient scanning using connection timeouts  
- Clear, structured output suitable for analysis  

## How It Works
The scanner iterates through a defined range of TCP ports and attempts to establish socket connections. Successful connections indicate open ports, while failed connections indicate closed or filtered ports. Timeout handling ensures that scanning large ranges remains efficient.

## Technologies Used
- Python  
- TCP/IP Networking  
- Socket Programming  

## Usage
1. Clone or download the repository.  
2. Run the script:  
   ```bash
   python portscanner.p
