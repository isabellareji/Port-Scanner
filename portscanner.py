
import socket
import argparse
from datetime import datetime

COMMON_SERVICES = {
    20: "FTP-data", 21: "FTP-control", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 67: "DHCP", 68: "DHCP",
    80: "HTTP", 110: "POP3", 143: "IMAP", 161: "SNMP",
    443: "HTTPS", 3306: "MySQL", 5432: "PostgreSQL",
}

def scan_ports(target="127.0.0.1", start_port=1, end_port=1024, timeout=0.4):
    open_ports = []
    print(f"Scanning {target} ports {start_port} to {end_port} (timeout {timeout}s)...\n")
    t0 = datetime.now()

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            try:
                result = sock.connect_ex((target, port))
                if result == 0:
                    service = COMMON_SERVICES.get(port, "")
                    open_ports.append((port, service))
                    print(f"  [OPEN]  Port {port} {('('+service+')') if service else ''}")
            except KeyboardInterrupt:
                print("\nScan cancelled by user.")
                break
            except Exception:
                # ignore other exceptions for this educational script
                pass

    t1 = datetime.now()
    duration = t1 - t0
    print(f"\nScan finished in {duration}.")
    print(f"Total open ports found: {len(open_ports)}")
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Simple educational port scanner (localhost only recommended).")
    parser.add_argument("--target", default="127.0.0.1", help="Target IP (default: 127.0.0.1)")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--timeout", type=float, default=0.4, help="Socket timeout seconds (default: 0.4)")
    args = parser.parse_args()

    if args.start < 1 or args.end > 65535 or args.start > args.end:
        print("Invalid port range. Ports must be 1-65535 and start <= end.")
        return

    open_ports = scan_ports(target=args.target, start_port=args.start, end_port=args.end, timeout=args.timeout)

    # Optional: show a summary in a compact way
    if open_ports:
        print("\nSummary:")
        for p, svc in open_ports:
            print(f" - Port {p}" + (f" ({svc})" if svc else ""))
    else:
        print("No open ports detected in the scanned range.")

if __name__ == "__main__":
    main()
