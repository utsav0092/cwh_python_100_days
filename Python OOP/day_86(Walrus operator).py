# """Walrus operator added in python 3.8 (:=)"""
#
# a = True
# print(a)
# print(a := False)
# print(a)
#
# numbers = [1, 2, 3, 4, 5]
# while (n := len(numbers)) > 0:
#     print(numbers.pop())

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = False
# print(happy)
#
# print(happy := True)
#
# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
