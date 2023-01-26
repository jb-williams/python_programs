import os
import socket

from Crypto.Cipher import AES

# need to be 16 bytes
key = b"TheNeuralNineKey"
nonce = b"TheNeuralNineNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connetct(("localhost", 9999))


file_size = os.path.getsize("somefile_mkv")

with open("somefile", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

client.send("newsomefile_mkv".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")

client.close()