l = [1, 3, 2, 5, 4]
print(l)

l.append(7)
print(l)
l.append(6)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(3))

print(l.count(2))

m = l
m[0] = 0
print(l)  # The main list will also change
print(m)

m = l.copy()
m[0] = 1
print(l)
print(m)

l.insert(1, 899)
print(l)

n = [900, 400, 600]
k = n + l
l.extend(n)  # Insert from the last
print(l)
print(k)
