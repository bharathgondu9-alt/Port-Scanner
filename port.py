import socket

target = input("Enter target IP or hostname: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

print("\nScan completed.")
