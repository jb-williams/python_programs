message = "Hello World! This is my message!"
#print(format(ord("A"), "b")) gets the ascii code of chars
binary = " ".join(format(ord(c), "b") for c in message)
#encoded
print(binary)

#decoded
binary_text = "".join(chr(int(c, 2)) for c in binary.split(" "))
print(binary_text)