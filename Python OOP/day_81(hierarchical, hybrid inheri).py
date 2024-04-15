# class Father:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f"Name : {self.name}")
#
#
# class Daughter(Father):
#     def __init__(self, name):
#         Father.__init__(self, name="Father")
#         self.name = name
#
#     def show(self):
#         Father.show(self)
#         print(f"Name : {self.name}")
#
#
# class Son(Father):
#     def __init__(self, name):
#         Father.__init__(self, name="Father")
#         self.name = name
#
#     def show(self):
#         Father.show(self)
#         print(f"Name : {self.name}")
#
#
# f = Son("Son")
# print(f.show())
# d = Daughter("Daughter")
# print(d.show())

class BaseClass:
    pass


class DerivedClass1(BaseClass):
    pass


class DerivedClass2(BaseClass):
    pass


class DerivedClass3(DerivedClass1, DerivedClass2):
    pass
