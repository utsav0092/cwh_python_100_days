f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        # print(line.type(line))
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks in {i} in {m1}")
    print(f"Marks in {i} in {m2}")
    print(f"Marks in {i} in {m3}")
    # print(line)
    # print(line)

# writelines()
# f = open('myfile3.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
