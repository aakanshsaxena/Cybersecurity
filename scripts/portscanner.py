import socket
import threading

openPorts = []
threads = []
target = input("Enter target IP address: ").strip()
if not target:
    print("No target IP address provided. Exiting.")
    exit()
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"\nScanning {target} from port {start_port} to {end_port}.\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            openPorts.append(port)
        s.close()
    except Exception as e:
        pass

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread) 
for thread in threads:
    thread.join()   

if openPorts:
    openPorts.sort()
    print(f"Open ports on {target}:")
    for port in openPorts:
        print(f"[+] Port {port} is open.")
else:
    print(f"No open ports found on {target}.")
