import re
import getpass
from fabric import Connection, Config

password = getpass.getpass("Enter Password: ")

config = Config(overrides={'sudo': {'password': password}})
# change ip and username to relevent values
conn = Connection("ip", user="user", config=config)

conn.run("ls -la")

result = conn.run("ls -la", hide=True)
print(result.stdout)

with conn.cd("/Documents"):
    conn.run("touch myfile.txt")
    conn.run("pwd")

# pass the pass once with getpass, then can call it with sudo()
conn.sudo("apt install vim")

conn.run("neofetch")


#example automation
result = conn.run("ifconfig")
lines = result.stdout.splut("\n")
inet_lines = [l for l in lines if "inet " in l and "127.0.0.1" not in l]
print(inet_lines)
span = re.search("inet ([0-9]+\.){3}[0-9+", inet_lines[0]).span()
print(span)
ip_address = inet_lines[0][span[0]+5:span[1]]
print(ip_address)