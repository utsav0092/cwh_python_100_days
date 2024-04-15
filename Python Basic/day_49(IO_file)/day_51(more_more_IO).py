# seek() and tell() functions

with open('myfile.txt', 'r') as f:
    print((type(f)))
    # Move to the 10th byte in the file
    f.seek(10)
    # Read the next 5 byte
    print(f.tell())  # tells the current position within the fies in bytes.(means kitne baad hai)
    data = f.read(5)
    print(data)


with open('sample', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)  # saves only up to this index

with open('sample.txt', 'r') as f:
    print(f.read())
