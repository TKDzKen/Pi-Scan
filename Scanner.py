import socket
import argparse
import threading
from Scanner_Imports import ping_sweep, single_ping

def art():
    ascii_art = r"""
     __________.___            _________                     
     \______   \   |          /   _____/ ____ _____    ____  
      |     ___/   |  ______  \_____  \_/ ___\\__  \  /    \ 
      |    |   |   | /_____/  /        \  \___ / __ \|   |  \
      |____|   |___|         /_______  /\___  >____  /___|  /
                                     \/     \/     \/     \/ 
  """
    print(ascii_art)


art()
print(("__") * 60)

#Scanner
def port_scan(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((ip, port))
            print(f"Port {port} is open on {ip}")
        except:
            pass
        finally:
            sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python offensive security tool for port scanning local or remote systems')
    parser.add_argument('--ip', type=str, help='Target ip address')
    parser.add_argument('--min_port', type=int, help='Minimum target port')
    parser.add_argument('--max_port', type=int, help='Maximum target port')
    parser.add_argument('--PS', type=str, help='Perform a ping sweep against the ip address range')
    parser.add_argument('--ping', type=str, help='Performs a ping against a singular ip address')
    args = parser.parse_args()

    # Multi-Threading
    threads = []
    if args.min_port is None or args.max_port is None:
        print("[!] Both min_port and max_port must be specified. use --help for more infomation.")
        ans = input("Would you like to test the default ports (Y/N): ")

        if ans in ["Y", "y", "yes", "Yes"]:
            args.min_port = 1
            args.max_port = 1000
        elif ans in ["N", "n", "no", "No"]:
            print("Exiting...")
            exit(1)
        else:
            exit(1)
    
    if args.min_port <= 0 or args.max_port <= 0:
        print("[!] Ports can not be 0 or less. Use --help for more infomation.")
        exit(1)
    for port in range(args.min_port, args.max_port + 1):
        thread = threading.Thread(target=port_scan, args=(args.ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
