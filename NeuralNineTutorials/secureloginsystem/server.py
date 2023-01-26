import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# user private ip
server.bind(("localhost", 9999))

server.listen()

def handle_conneciton(c):
    # normally would want to encrypt transmission, encrypt connection even better
    # this focused on sec of database itself
    # if exchanging pub and private keys just encrypt the send and recv
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    # here important to use prepared statements due to sql injection
    cur.execut("SELECT * FROM userdata WHERE username = ? AND passowrd = ?", (username, password))

    if cur.fetchall():
        c.send("Login successful!".encode())
        # secrets 
        # services
    else:
        c.send("Login failed!".encode())

while True:
    client, add = server.accept()
    threading.Thread(target=handle_conneciton, args=(client,)).start()