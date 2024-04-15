# Tuples are immutable in nature

# Change the elements in the tuple using lists
countries = ("Spanish", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)


# We can concatenate two tuples creating the third tuple
new1 = ("hi", "there", "how")
new2 = ("are", "you")
new3 = new1 + new2
print(new3)

'''
new1.count(no. of occurrences)

print the first occurrence of the data if not present error :-
new1.index(3)
new1.index(3 occur, 4 from, 8 to) 

len(new1)
'''