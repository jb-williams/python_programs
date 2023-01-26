import time
import pyotp

key = pyotp.random_base32()
key1 = "NeuralNineMySuperSecretKey"

print(key)
print(key1)

# TOTP
totp = pyotp.TOTP(key1)

print(totp.now())

#time.sleep(30)
#print(totp.now())

input_code = input("Enter 2FA Code: ")

print(totp.verify(input_code))