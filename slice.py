#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import os
import sys
import time
import random
import string
#written by Leonidus feel free to imporve it <3
#cuz it honestly sucks :p
#hack the planet!!!
slice = """
 
\033[1;31;40m  ██████  ██▓     ██▓ ▄████▄  ▓█████ \033[1;31;40m
\033[0;33;40m▒██    ▒ ▓██▒    ▓██▒▒██▀ ▀█  ▓█   ▀ \033[1;33;40m
\033[1;32;40m░ ▓██▄   ▒██░    ▒██▒▒▓█    ▄ ▒███ \033[1;32;40m
\033[1;36;40m  ▒   ██▒▒██░    ░██░▒▓▓▄ ▄██▒▒▓█  ▄ \033[1;36;40m
\033[1;36;40m▒██████▒▒░██████▒░██░▒ ▓███▀ ░░▒████▒ \033[1;36;40m
\033[1;31;40m▒ ▒▓▒ ▒ ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░░░ ▒░ ░ \033[1;31;40m
\033[1;31;40m░ ░▒  ░ ░░ ░ ▒  ░ ▒ ░  ░  ▒    ░ ░  ░ \033[1;31;40m
\033[1;31;40m░  ░  ░    ░ ░    ▒ ░░           ░ \033[1;31;40m
\033[1;31;40m      ░      ░  ░ ░  ░ ░         ░  ░ \033[1;31;40m
\033[1;31;40m                     ░ \033[1;31;40m
 
"""
info = """
read the code to see what it does, its quite simple really.
just checks for common open ports and connects to check the status
of the host ~Leonidus
"""
if len(sys.argv) < 2:
    print slice + info
    print "[+] Usage: python "+sys.argv[0]+" <hostname>"
    sys.exit()
print slice
ip = sys.argv[1]
ports = ["53", "80", "1194", "8080"]
kek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checks if desired ports are open for further testing of status
def sector(port):
    try:
        con = kek.connect((ip, int(port)))
        return True
    except:
        return False
for fag in ports:
    if sector(fag):
        open1 = ("\033[1;32;40m [+] port %s is open \n" % fag)
        print open1
    else:
        closed1 = ("\033[1;31;40m [-] port closed \n")
        print closed1
kek.close()
if __name__ == "__sector__":
    sector()
 
 
#continue
jack = raw_input("\033[1;32;40m [+] continue? y/n: ")
if jack == "y":
    os.system("clear")
    print slice
    print open1
    spec_port = raw_input("[+] Choose port you're attacking: ")
else:
    print("closing script")
    os.kill(os.getpid(), 9)
 
#checking status of host via port
while True:
    p = random.choice(string.letters+string.digits)
    fuck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        time.sleep(1)
        fuck.settimeout(3)
        fuck.connect((ip, int(spec_port)))
        print("\033[1;32;40m [-] host is alive! %s\n" % p)
    except:
        print("\033[1;31;40m [+] seems to be down <3")
