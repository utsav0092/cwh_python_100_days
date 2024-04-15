name = "Harry"
print(name[:5])  # 0 to 4 (slicing of string)
print(name[0:3])
print(len(name))  # length of whole string
print(name[:])
print(name[0:-3])  # will count from last
print(name[-1:-3])  # total length - 1 to total length - 3
print(name[-3:-1])
print(name[0:len(name)-3])
for i in range(len(name)):
    print(name[i])
print(name[-4:-2])
