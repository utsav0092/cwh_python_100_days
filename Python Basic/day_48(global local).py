x = 4
y = 10
print(x)


def hello():
    global x  # set the global variable or change the existing global variable
    x = 5
    # y = 7  #  It is a local variable in this function
    print(x)
    print(f"The global y value in hello function is {y}")
    print(f"The local x is {x}")
    print(f"Hello harry")


print(f"The global x is {x}")


hello()
print(f"The global x is {x}")
