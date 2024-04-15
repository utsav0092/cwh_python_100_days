class Employee:
    companyName = "Apple"
    noEmployee = 0

    def __init__(self, name):
        self.name = name
        self.amount = 0.02
        Employee.noEmployee += 1

    def showname(self):
        print(f"The name is {self.name} and amount is {self.amount} and company name is {self.companyName} and consists {self.noEmployee}")


emp = Employee("Harry")
emp.amount = 0.4
emp.companyName = "Apple India"
# emp.showname()
Employee.showname(emp)
emp2 = Employee("Rohan")
emp2.companyName = "Apple USE"
emp2.showname()
