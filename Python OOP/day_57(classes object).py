class Person:
    name = "5Star"
    work = "Do Nothing"

    def into(self):  # everytime self will be the first parameter
        print(f"name = {self.name} \nwork = {self.work}")


a = Person()  # object of the class
a.name = "New 5Star"
a.work = "Still Do Nothing"
# print(a.name+"\n"+a.work)
a.into()
