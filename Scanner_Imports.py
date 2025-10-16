from scapy.layers.inet import IP, ICMP
from scapy.all import sr1
import ipaddress 

def ping_sweep(ip, timeout=3):
    try:
        ipaddress.ip_network(ip + '.0')
    except ValueError:
        print(f"Invalid IP address: {ip}")
        return

    print(f"Performing Ping Sweep on {ip}.0/24")
    for j in range(0, 256):
        net = f"{ip}.{j}"
        pk = IP(dst=net) / ICMP()
        try:
            rep = sr1(pk, timeout=timeout, verbose=0)
            if rep:
                print(f"Host {net} is up")
            else:
                print(f"Host {net} is down or unresponsive")
        except Exception as e:
            print(f"Error pinging {net}: {e}")

def single_ping(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"Invalid IP address: {ip}")
        return

    pk = IP(dst=ip) / ICMP()
    try:
        rep = sr1(pk, timeout=5, verbose=0)
        if rep:
            print(f"Host {ip} is up")
        else:
            print(f"Host {ip} is down or unresponsive")
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
