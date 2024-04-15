class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


e = Employee("Harry", 12000)
print(e.name)
print(e.salary)
string = "Harry-12000"
print(string.split("-"))
# e2 = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
