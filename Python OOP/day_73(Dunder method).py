class Person:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        c = 0
        for c in self.name:
            c = c + 1
        return c

# Can be call from another file as well
    def __str__(self):
        print(f"The name of employee is {self.name} __str__")

# If __str__ does not work then __repr__ will work
    def __repr__(self):

        # print(f"The name of employee is {self.name} repr")
        return f"Person '{self.name}'"

# It will print on object call like p()
    def __call__(self, *args, **kwargs):
        print("Hey it is call")


p = Person("Harry")
print(p)
print(p.name)
print(len(p))


"""
In another file emp.py

from emp import Person
p = Person("Harry")
print(p)
print(str(p))
print(repr(p))
p()
"""
