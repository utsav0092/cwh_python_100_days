class NewPerson:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
        self.info()

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = NewPerson("Harry", "Developer")   # parameterized constructor
a.name = "Divya"
a.occ = "HR"
a.info()
