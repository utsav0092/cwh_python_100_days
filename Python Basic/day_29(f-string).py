# This feature come in python in 3.6 version
letter = "Hey my name s {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))

# Using the f-strings format
print(f"Hey my name is {{name}} and I am from {{country}}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.0099999))
print(txt)
price = 49.09999
print(f"For only {price:.2f} dollars!")

print(f"{2 * 30}")
print(type(f"{2 * 30}"))

t = "there"
h = "how"
letter2 = f"Hi {t}, {h} are you"
print(letter2)
