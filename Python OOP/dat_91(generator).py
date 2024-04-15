def my_generator():
    for i in range(5):
        """instead return we yield that returns a generator 
           and suspends the execution until the next value is requested."""
        yield i


gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)
