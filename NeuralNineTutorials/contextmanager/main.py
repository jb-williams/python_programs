# implementing own context manager example 
class FileStream:

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.filestream = open(self.path, self.mode)
        return self.filestream

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.filestream.close()

with FileStream("file.txt", "w") as f:
    f.write("Other text")

print(f.closed)

## /\ same functionality as \/

# likely better practice
from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with filestream("file.txt", "w") as file:
    file.write("Again another text")

print(file.closed())