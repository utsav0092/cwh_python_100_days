"""dir() method"""

a = [1, 2, 3]
print(dir(a))
print(a.__add__)

"""dict method"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Harry", 45)
print(p.__dict__)

"""help() method"""

print(help(Person))
