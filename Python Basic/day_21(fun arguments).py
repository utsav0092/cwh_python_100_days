# There are 4 types of arguments in function:
# 1. required arguments:
def average(a,b):
    print("The average is : ", (a+b)/2)
average(3,3)

# 2. default arguments:
def average(a,b=1):
    print("The default average is : ", (a+b)/2)
average(3,3)

# 3. keyword arguments:
def average(a,b):
    print("The average is : ", (a+b)/2)
average(b=5,a=5)
# 4. taking it as tuple:
def avav(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print("Sum is : ", sum/len(number))
avav(5,6)

# 5. taking as dictionary:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Buchan", lname="Brans", fname="Jams")