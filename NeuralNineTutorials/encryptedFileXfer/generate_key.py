from Crypto.Cipher import AES

# need 16 bytes for each of these
key = b"TheNeuralNineKey"
nonce = b"TheNeuralNineNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext = cipher.encrypt(b"Hellow Workd!")

print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(ciphertext))