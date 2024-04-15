import requests
from bs4 import BeautifulSoap

# response = requests.get("https://www.codewithharry.com")
# print(response.text)

"""Post request"""
# url = "https://jsonplaceholder.tyicode.com/posts"
#
# data = {
#     "title": 'Harry',
#     "body": 'bhai',
#     "userId": 12,
# }
#
# headers = {
#     'Content-type': 'application/json; charset=UTF-8'
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# print(response.text)

url = 'https://www.codewithharry.com/blogpost/django-cheatsheets/'
r = requests.get(url)
# print(r.text)

for heading in soup.find_all("h2"):
    print(heading.text)

soup = BeautifulSoap(r.text, 'html.parser')

print(soup.prettify())
