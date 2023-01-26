import socket
import threading
# will have buffer overflow error if message is too big

import rsa

public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server.bind(("localhost", 9999))
    # over internet this would be your pub ip
    server.bind(("192.168.0.164", 9999))
    server.listen()

    client, _ = server.accept()

    client.send(public_key.save.pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # over internet other person would specify your pub ip
    # or you specifying their pub ip to connect to them
    client.connect(("192.168.0.164", 9999))

    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save.pkcs1("PEM"))
else:
    exit()

def sending_messages(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(), public_key))
        # to test in wireshark
        #c.send(message.encode())
        print("You: " + message)

def receiving_messages(c):
    while True:
        message = input("")
        print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())
        # to test in wireshark
        #print("Partner: " + c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()