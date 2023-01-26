
# this is not best way
# try to handle exceptions and close
file = open("file.txt", "w")
try:
    file.write("Hello World")
    print(file.closed)
finally:
    file.close()

print(file.closed)

# better way "with", once leaving "with" block file closes
with open("file.txt", "w") as f:
    f.write("hello world")

print(f.closed)