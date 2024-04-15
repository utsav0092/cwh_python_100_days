def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)
def largerNum(a,b):
    if a>b:
        print("a is big")
    else:
        print("b is big")
def smallerNum(a, b):
    pass  # without any error it will execute

a = 8
b = 9
calculateGmean(a, b)
largerNum(a, b)
# gmean = (a*b)/(a+b)
# print(gmean)
c = 8
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)
largerNum(c, d)