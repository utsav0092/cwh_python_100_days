# class Person:
#     def __init__(self):
#         self.__name = "Harry"
#
#
# a = Person()
# # print(a._name)  # Protect member of a class and cannot be access directly
# print(a._Person__name)  # can be accessed indirectly (name mangling)
# print(a.__dir__())

class Student:
    def __init__(self):
        self.__name = "Harry"  # protected variable

    def _func_name(self):
        return "CodeWithHarry"  # protected method


class Subject(Student):
    pass


obj = Student()
print(obj._Student__name)
obj1 = Subject()
