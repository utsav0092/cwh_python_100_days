a = int(input("Enter your age : "))
print("Your age is  : ", a)
# >,<,<=,>=
if a > 18:
    print("You can drive")
elif a < 0:
    print("The number is negative")
elif a == 18:
    print("You can drive")
elif a == 0:
    print("This is not possible")
else:
    print("You can drive")
