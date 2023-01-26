# Will require dependencies
# Docker installed and Daemon Running
# to run, nav to where the script and dockerfile are, in Terminal
# docker build -t [container_name] .

# then, docker run -p [port]:[port] [container_name]

#ex:
#   docker build -t iris-dockerization .

# then, docker run -p 9999:9999 iris-dockerization

# install scikit-learn to containerize,
#  it then you can uninstall package from system and will still work in the docker container

#pip3 install scikit-learn

# can connect with netcat

import time
import socket
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from ", addr)
    client.send("You are connected!\n".encode())
    client.send(f"{data['data'][:, 0]}\n".encode())
    time.sleep(2)
    client.send("You are being disconnected!\n".encode())
    client.close()