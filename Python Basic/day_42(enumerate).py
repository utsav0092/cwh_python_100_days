marks = [12, 23, 34, 45, 56, 67, 78]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Harry awsome!")
#     index += 1

for index, mark in enumerate(marks, start=3):
    print(mark)
    if index == 3:
        print("Harry")
