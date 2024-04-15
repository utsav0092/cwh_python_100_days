# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")
#
# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("harry")
#         super().parent_method()
#     def child_method(self):
#         print("This is child method")
#         super().parent_method()
#
# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()


class Base1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Base2(Base1):
    def __init__(self, name, age, work):
        super().__init__(name, age)
        self.work = work


rohan = Base1("Rohan", 450)
harry = Base2("Harry", 56, "python")
print(harry.name)
print(harry.age)
print(harry.work)
