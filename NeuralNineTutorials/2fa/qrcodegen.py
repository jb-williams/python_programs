import time
import pyotp
import qrcode

key1 = "NeuralNineMySuperSecretKey"

print(key1)

uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSome123", issuer_name="NeuralNine App")

print(uri)

qrcode.make(uri).save("totp.png")

# use this as another script to verify functionality of above in your auth app

key = "NeuralNineMySuperSecretKey"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter code: ")))