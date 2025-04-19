import socket
from datetime import datetime

def scan_ports(target_ip, port_range=(1, 1024)):
    print(f"\n🔍 Scanning target: {target_ip}")
    print(f"Scanning ports {port_range[0]} to {port_range[1]}...\n")
    start_time = datetime.now()

    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown service"
                print(f"✅ Port {port} OPEN  ({service})")
            sock.close()
        except socket.error:
            print(f"❌ Couldn't connect to port {port}")

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n⏱️ Scan completed in: {duration}")

if __name__ == "__main__":
    print("🛠️ Simple Port Scanner")
    target = input("Enter an IP address to scan: ")

    try:
        scan_ports(target)
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
    except socket.error:
        print("❌ Couldn't connect to target.")
