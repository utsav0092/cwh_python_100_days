# Lamda function are used for creating anonymous function

# Functions can also be taken as argument
def appl(fx, value):
    return 6 + fx(value)  # take both function and value

double = lambda x: x**2
SUM = lambda x, y: x+y
AVG = lambda x, y, z: (x+y+z)/3
print(double(5))
print(SUM(4, 4))
print(AVG(2, 2, 2))
print(appl(lambda x: x*x, 2))
