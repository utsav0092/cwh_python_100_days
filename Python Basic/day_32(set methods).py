s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 7, 8, 9, 0}

print(s1.union(s2))

# s1.update(s2)

print(s1, s2)

print(s1.intersection(s2))

name = {1, 2, 3, 4, 5}
NAME = {2, 4, 6, 8, 0, 5}
name.intersection_update(NAME)
print(name)

name = {1, 2, 3, 4, 5, 12, 23, 45, 56, 67, 78, 89}
# NAME = {2,4,6,8,0,5}
NAME = {12, 23, 45, 56}
Name = name.symmetric_difference(NAME)
print(Name)
print(NAME.isdisjoint(name))
print(NAME.issuperset(name))
print(NAME.issubset(name))

NAME.add(100)
print(NAME)

NAME.remove(100)
print(NAME)

NAME.discard(80)

item = NAME.pop()
print(item)
print(NAME)

del NAME
name.clear()
print(name)
