dic = {122: 45, 123: 89, 124: 45}
dic2 = {222: 32, 223: 43, 224: 54}

print(dic[122])
print(dic[123])
print(dic[124])

print("------------------------------")

dic.update(dic2)
print(dic)

print("------------------------------")

dic.clear()
print(dic)

print("------------------------------")

dic2.pop(222)
print(dic2)

print("------------------------------")

dic2.popitem()  # remove the last value
print(dic2)

print("------------------------------")

# def dic will delete the whole dictionaries
del dic2[223]
print(dic2)
