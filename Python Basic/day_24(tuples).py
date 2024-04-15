# It is immutable in nature

t = (1, 2, 3, 4, 5, 323)
print(type(t), t)

print(len(t))

print(t[-1])

# tup = (1)  # Treated as int instead use (1,)
# print(type(tup), tup)

# t[0] = 90  # can't be assign in tuple
# print(type(t), t)

if 323 in t:
    print("Yes 323 it is there")

tup = t[1:4]  # slicing the tuple
print(tup)
