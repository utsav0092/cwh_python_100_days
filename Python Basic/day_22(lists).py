List = [1, 2, 3, 4, 5]
print("It is a list : ", List)
print(type(List))
Set = {1, 2, 3, 4, 5}
print("It is a set : ", Set)
print(type(Set))
Tuple = (1, 2, 3, 4, 5)
print("It is a tuple : ", Tuple)
print(type(Tuple))

# It is mutable

marks = [3, 4, 5, "Harry", True, 23, 45, 56, 67, 78, 98]
# marks[0] = 5
# marks[1] = 4
# marks[2] = 3
print(marks[len(marks)-2])
print(marks[5-3])
print(marks[0], marks[1], marks[2], marks[3], marks[4])
print(marks)
print(marks[0:11:2])  # Jump statement
print((marks[1:-1]))

if "Harry" in marks:
    print("Yes")
else:
    print("No")

if "ary" in "Harry":
    print("Yes")
else:
    print("No")

lst = [i * i for i in range(5)]  # list comprehension statement
print(lst)

lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)
