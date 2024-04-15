# A basic string input.
string = input('Enter the string : ')
print('The string is : ', string)
name = 'name'
name1 = 'I am a "name" '
name2 = "I am another \"name\""
name3 = '''hi there'''
print(name1)
print(name2)
print(name3)
string2 = """string = input('Enter the string : ')
print('The string is : ', string)
name1 = 'I am a "name" '
name2 = "I am another \"name\""
name3 = '''hi there'''
print(name1)
print(name2)
print(name3)
print('Hello ' + name1)
"""
print('Hello ' + name1)
print(string2)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print whole string using a for(string) loop
print('Using loop : ')
for char in string:
    print(char[0])