import os
print("Hello world from...")
os.system("Python --version")

x = int(input("Enter the value of x : "))
match x:
    case 0:
        print("The value is 0")
    case 1:
        print("It is 1")
    case 2:
        print("It is 2")
    case _ if x != 90:
        print(x, "Is not 90")
    case _ if x != 80:
        print(x, "Is not 80")
    case _:
        print(x)
