import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTERGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "matt123", hashlib.sha256("mattpassowrd".encode()).hexdigest()
print(password1)
username2, password2 = "john", hashlib.sha256("johnpassowrd".encode()).hexdigest()
username3, password3 = "jack", hashlib.sha256("jackpassowrd".encode()).hexdigest()
username4, password4 = "phil", hashlib.sha256("philpassowrd".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

