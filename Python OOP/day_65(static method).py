class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

# can be used without creating instance of the class
# No need of self in static methods
# Can be called by class name also
    @staticmethod
    def add(a, b):
        return a + b


# result = Math.add(a, b)
a = Math(5)
print(a.num)
a.addtonum(5)
print(a.num)
print(a.add(5, 5))
print(Math.add(5, 5))
