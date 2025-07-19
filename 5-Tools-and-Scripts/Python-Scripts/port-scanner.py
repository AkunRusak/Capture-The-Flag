# ============================================
# PORT SCANNER
# ============================================
import socket
from datetime import datetime

def port_scan(target, ports):
    print(f"Scanning {target}")
    print(f"Started at {datetime.now()}")
    print("-" * 50)
    
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: Open")
            open_ports.append(port)
        
        sock.close()
    
    print("-" * 50)
    print(f"Scan completed. Open ports: {open_ports}")
    return open_ports

# Usage
# common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995]
# port_scan("127.0.0.1", common_ports)