class Employee:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def show_details(self):
        print(f"The name is {self.name} and id  {self.value}")


class Programmer(Employee):
    def show_language(self):
        print(f"The default language is python")


e = Employee("Rohan", 400)
e.show_details()
E = Employee("Harry", 4100)
E.show_details()
p = Programmer("H", 23)
p.show_details()
