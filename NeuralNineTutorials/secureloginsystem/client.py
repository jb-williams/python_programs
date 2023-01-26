import socket
# obviously connect to public, host on private

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# use public ip
client.connect(("localhost", 9999))

message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(input(message).encode())
print(client.recv(1024).decode())