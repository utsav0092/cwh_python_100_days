# Topic DocStrings and pep - 8
# Docstring appear just after the definition of functions, methods, modules, etc.

def square(n):
    # print(n)
    # It is used for comments
    # """ It is used for DocStrings"""
    """Takes in a number n, returns the square of n"""
    print("The square of number is : ", n**2)


square(5)
print(square.__doc__)
# In terminal 1.python, 2.import this.
