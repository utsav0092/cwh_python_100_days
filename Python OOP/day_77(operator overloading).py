class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, v):
        return Vector(self.i + v.i, self.j + v.j, self.k + v.k)


class newVector(Vector):

    def __add__(self, o):
        x = 12
        y = 32
        z = 54
        return newVector(self.i + o.x, self.j + o.y, self.k + o.z)


obj1 = Vector(2, 3, 5)
obj2 = Vector(2, 3, 5)
print(obj1)
print(obj2)
Add = obj1 + obj2
print(Add)
print(type(Add))
ut = newVector(2, 2, 2)
print(ut)

