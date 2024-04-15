txt = "The beast things in life are free!"
print("free" in txt)

txt = "The beast things in life are free!"
if "free" in txt:
    print('Yes free is present')

txt = "The beast things in life are free!"
print("expensive" not in txt)

txt = "The beast things in life are free!"
if "expensive" not in txt:
    print("No it is not present")

name = "  Code With Harry"
Name = "  Coder"
print(name.upper())
print(name.lower())
print(name.strip())  # remove spaces from beginning or the end
print(name.replace('C', 'H'))
print(name.split())  # split the given string
c = name + " " + Name
print(c)
print(name + Name)

age = 34
txt = "My nane is John, and I am {}"
print(txt.format(age))
num = 23
Ok = "OK {}, it was {}, just {}"
print(Ok.format(num, num, num))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
name = "hello world hi there"
print(name.title())
print(name.istitle())
