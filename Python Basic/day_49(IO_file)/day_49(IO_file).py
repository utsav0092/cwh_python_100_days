"""Read mode (r)"""
# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# Using direct write will delete the existing text and add new given text
# to resolve this we should use append("").
# filetypes :- r w a rb rt

"""Write mode (w)"""
# f = open('myfile2.txt', 'w')
# f.write("This is a new file")
# f.close()

"""Append mode (a)"""
# f = open('myfile2.txt', 'a')
# f.write("This is a new file now it was in append mode")
# f.close()

# with open('myfile.txt', 'a') as f:
#     f.write("I am inside mufile.txt")
