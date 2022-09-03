#!/usr/bin/env python3
## email client tutorial on freecode.com done by neuralNine

## ONLY RUN THIS ON YOUR HOMELAB OR SOMEWHERE THAT GAVE YOU PERMISSION TO
## Running this on anything that you DO NOT have Explicit Written Permission to do so!
## This is only for Educational Purposes, This IS ILLEGAL without permission, coming with potential jail time.
## this is not an optimal script it just concept, would not be used in "real" life

import socket
import threading
from queue import Queue # this is to que the elements/list of ports so you done duplicate ports

## again only run this on your own equipment just to be safe
## this is hardcoded in and can be changed depending on the test target
## this would be to scan your host computer
#target = "127.0.0.1"
target = "10.0.0.138"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

## doing it like this would be more basic and doing specific single ports
#print(portscan(80))

## this goes through the standard used ports all ports would be the ~64738
## this is very slow as going one port at a time
#for port in range(1, 1024):
#    result = portscan(port)
#    if result:
#        print("Port {} is open!".format(port))
#    else:
#        print("Port {} is closed!".format(port))

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

## worker or handler method
def handler():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

## to fill the queue, range is whichever range from 1-64k or so that you want to scan
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

## the amount of threads to run 10 = ~10 ports per second, adjust to how you see fit
## could keep increasing it until it won't get any faster and may cause slowing
for t in range(100):
    ## creating threads where their target function is the handler
    thread = threading.Thread(target=handler)
    thread_list.append(thread)

## starts each thread
for thread in thread_list:
    thread.start()

## this with the thread list makes sure that all threads finish before the print at the end
for thread in thread_list:
    thread.join()

## should be printed after all threads have been completed
print("Open ports are: ", open_ports)
