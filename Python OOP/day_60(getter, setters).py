# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def show(self):
#         print(f"The value is {self._value}")
#
#     @property
#     def value(self):
#         return 10 * self._value
#
#     # @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
#
#
# a = MyClass(1)
# a.ten_value = 60
# print(a.ten_value)
# # print(a.value)
# a.show()

class Person:
    def __init__(self, value):
        self._value = value

    @property
    def ten_value(self):
        print(f"The initial value is {self._value}")
        return self._value

    @ten_value.setter
    def ten_value(self, value):
        print(f"The {self._value} is equal to {value}")
        self._value = value

    @ten_value.deleter
    def ten_value(self):
        print(f'The "{self._value}" was deleted')
        del self._value


if __name__ == '__main__':
    p = Person('Harry')
    print(p.ten_value)
    p.ten_value = 12
    del p.ten_value
