dic = {
    1: "NAME",
    2: "name",
    3: "Name",
    4: "nAME"
    # key: "value"
}
print(dic[1])
print(dic[2])
print(dic[3])
print(dic[4])

print("----------------------------")

print(dic.get(4))  # instead error print None

print("----------------------------")

print(dic.keys())
print(dic.values())
for key in dic.keys():
    # print(dic[key])
    print(f"The values corresponding to the key {key} is {dic[key]} ")

print("-------------------------------")

print(dic.items())
for key, value in dic.items():
    print(f"The values is {key} is {value} ")
