class Main:
    name = "Apple"

    def show(self):
        print(f"The name is {self.name}")

    # Changes the class variable using @classmethod and cls (class)
    @classmethod
    def changeCompany(cls, newcompany):
        cls.name = newcompany


e1 = Main()
e1.name = "Harry"
e1.show()
e1.changeCompany("Google")
e1.show()
print(Main.name)
