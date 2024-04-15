a = int(input("Enter the value between 5 to 10 : "))
if a < 5 or a > 10:
    raise ValueError("Value should be between 5 to 10 only")

string = input("Enter word quit or QUIT : ")
if "quit" == string or "QUIT" == string:
    print("Thank you")
else:
    raise ValueError("It is not word quit")
