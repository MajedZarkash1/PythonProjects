#options
"""
File Name: port_scanner.py
Author: Your Name
Purpose: A script to scan specified ports on a target IP or hostname.
Development Start Date: YYYY-MM-DD
Development End Date: YYYY-MM-DD
"""

import socket
import logging
from datetime import datetime

def setup_logging():
    """Sets up logging for the script."""
    logging.basicConfig(
        filename="port_scan.log", 
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def scan_port(target, port):
    """Attempts a TCP connection to a given port on the target."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                logging.info(f"Port {port} is open on {target}")
                return port
    except Exception as e:
        logging.error(f"Error scanning port {port} on {target}: {e}")
    return None

def scan_ports(target, start_port, end_port):
    """Scans a range of ports on a given target and reports open ports."""
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scanned_port := scan_port(target, port):
            print(f"Port {scanned_port} is open")
            open_ports.append(scanned_port)
    if not open_ports:
        print("No open ports found.")
    return open_ports

def main():
    """Main function to handle user input and initiate scanning."""
    setup_logging()
    target = input("Enter target IP or hostname: ")
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port > end_port or start_port < 0 or end_port > 65535:
            print("Invalid port range. Ensure start port is less than end port and within 0-65535.")
            return
    except ValueError:
        print("Invalid input. Please enter numerical values for ports.")
        return
    scan_ports(target, start_port, end_port)

if __name__ == "__main__":
    main()

