# # def cube(x):
# #     return x * x * x
# l1 = [1, 2, 3, 4, 5]
# # l2 = []
# # for item in l1:
# #     l2.append(cube(item))
# """Map"""
# l2 = list(map(lambda x: x * x * x, l1))  # typecasting required, returns map object
# print(l2)
#
# """Filter"""
# # def filter_function(a):
# #     return a > 4
# l3 = list(filter(lambda x: x > 2, l1))
# print(l3)
#
# """Reduce"""
# # def Sum(x, y):
# #     return x + y

from functools import reduce

number = [1, 3, 2, 5, 9, 6]
Sum = reduce(lambda x, y: x+y, number)
print(Sum)

"""It all are higher order functions as they take other functions as arguments"""
