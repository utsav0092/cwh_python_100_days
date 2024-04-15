question = [
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3],
    ["FaceBook was invented using which language ? ", "Python", "Java", "ReactJs", "None", 3]
    ]

level = [1000, 2000, 3000, 5000, 10000, 15000, 30000, 50000, 100000, 1500000, 5000000, 10000000]
money = 0
for i in range(0, len(question)):
    questions = question[i]
    print(f"\n\nQuestion for Rs.{level[i]}")
    print(f"Question : {questions[0]}")
    print(f"a. {questions[1]}        b. {questions[2]}")
    print(f"c. {questions[3]}        d. {questions[4]}")

    replay = int(input("Enter your answer (1 -4) : "))
    if replay == questions[-1]:
        print(f"Your answer is correct you have won Rs.{level[i]}")
        if i == 4:
            money = 10000
        elif i == 8:
            money = 10000
        elif i == 11:
            money = 100000
    else:
        print(f"Your answer is wrong the right answer is : {questions[-1]}")
        print(f"You are going home with Rs.{money}")
        break
