num = int(input("Enter the number : "))
for i in range(num):
    print(i)

name = "NAME"
for i in name:
    print(i, end="~")

for i in "Harry":
    print(i)

colors = ["red", "yellow", "blue", "purple"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(1, 10, 2):
    print(k)
