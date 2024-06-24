#!/usr/bin/python3
import subprocess
import socket
import argparse
import threading

#clearing screen
subprocess.call("clear", shell=True)

#Welcome message
def Art():
    ascii_art = r"""
     __________.___            _________                     
     \______   \   |          /   _____/ ____ _____    ____  
      |     ___/   |  ______  \_____  \_/ ___\\__  \  /    \ 
      |    |   |   | /_____/  /        \  \___ / __ \|   |  \
      |____|   |___|         /_______  /\___  >____  /___|  /
                                     \/     \/     \/     \/ 
  """
    print(ascii_art)

Art()

print("""Pi-scan
      Created by Kenyon Bias""")
print(("__")*60)

#scanner
def port_scan(IP, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, port))
        print(f"Port {port} is open on {IP}")
    except:
        pass
    finally:
        sock.close()

#arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A Base level python port scanner')
    parser.add_argument('--IP', type=str, help='Remote target IP address')
    parser.add_argument('--min_port', type=int, help='Minimum remote target port')
    parser.add_argument('--max_port', type=int, help='Maximum remote target port')
    args = parser.parse_args()
    

#multi-threading
    threads = []
    for port in range(args.min_port, args.max_port + 1):
        thread = threading.Thread(target=port_scan, args=(args.IP, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
