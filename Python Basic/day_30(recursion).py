def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print("The factorial is : ", factorial(5))
print("The factorial is : ", factorial(4))
print("The factorial is : ", factorial(3))
print("The factorial is : ", factorial(2))
print("The factorial is : ", factorial(1))
print("The factorial is : ", factorial(0))

# f0 = 0
# f1 = 1
# f2 = f1 + f0
# f(n) f(n-1) + f(n-2)


def fibo(n):
    if n <= 0:
        print('Incorrect Input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))
