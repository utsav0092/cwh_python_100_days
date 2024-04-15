"""It is Regular expressions, it is a wide field pyton docs for learning and Regxr website"""
import re

pattern = r"[A-Z]+ommons"
text = '''If you are browsing Commons for the first time, you may want to start with Featured pictures, Quality images, 
Valued images or Featured media. BommonsYou can also see some work created Sommons by our highly skilled contributors'''
# match = re.search(pattern, text)
# print(match)
matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])
