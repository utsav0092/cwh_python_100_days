try:
    l = [1, 2, 3, 4]
    n = int(input("Enter the index value : "))
    print(l[n])
except:
    print("Error found")
finally:
    print("I will always run")


def func():
    try:
        l = [1, 2, 3, 4]
        n = int(input("Enter the index value : "))
        print(l[n])
        return 1
    except:
        print("Error found")
        return 0
    finally:
        print("I will always run")


x = func()
print(x)
