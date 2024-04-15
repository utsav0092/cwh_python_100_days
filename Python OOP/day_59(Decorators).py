def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thank you")
    return mfx


@greet  # Decorator
def hello():
    print("Hello world")


def add(a, b):
    print(a + b)


# greet(hello())
hello()
add(1, 2)


