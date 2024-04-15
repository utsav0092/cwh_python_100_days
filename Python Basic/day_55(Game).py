# import random
#
# while True:
#     Input = str(input("Enter your move (Stone, Paper, Scissors) : ").lower())
#     c_move = None
#     count = 0
#     if Input == "scissors":
#         C_move = random.randrange(1, 100)
#         if C_move <= 40 and C_move >= 1:
#             c_move = "scissors"
#             print("Bot : ", c_move)
#         elif C_move <= 80 and C_move > 40:
#             c_move = "paper"  # paper
#             print("Bot : ", c_move)
#         elif C_move <= 100 and C_move > 80:
#             c_move = "stone"  # stone
#             print("Bot : ", c_move)
#         if c_move == "paper":
#             count += 1
#             print("You Won")
#         elif c_move == "scissors":
#             print("Its a draw")
#         else:
#             print("You Lose")
#
#     elif Input == "paper":
#         C_move = random.randrange(1, 100)
#         if C_move <= 40 and C_move >= 1:
#             c_move = "scissors"  # sites
#             print("Bot : ", c_move)
#         elif C_move <= 80 and C_move > 40:
#             c_move = "paper"  # paper
#             print("Bot : ", c_move)
#         elif C_move <= 100 and C_move > 80:
#             c_move = "stone"  # stone
#             print("Bot : ", c_move)
#         if c_move == "paper":
#             print("Its a draw")
#         elif c_move == "scissors":
#             count += 1
#             print("You Won")
#         else:
#             print("You Lose")
#
#     elif Input == "stone":
#         C_move = random.randrange(1, 100)
#         if C_move <= 40 and C_move >= 1:
#             c_move = "scissors"  # sites
#             print("Bot : ", c_move)
#         elif C_move <= 80 and C_move > 40:
#             c_move = "paper"  # paper
#             print("Bot : ", c_move)
#         elif C_move <= 100 and C_move > 80:
#             c_move = "stone"  # stone
#             print("Bot : ", c_move)
#         if c_move == "paper":
#             count += 1
#             print("You Won")
#         elif c_move == "scissors":
#             print("You Lose")
#         else:
#             print("Its a draw")
#
#     else:
#         print("Invalid Choice :/")
#
#     IInput = input("Do you want to play again if y/n : ")
#     if IInput.lower() == 'y':
#         continue
#     elif IInput.lower() == 'n':
#         print("You won ", count, "times")
#         print("Thank you for playing please visit again :)")
#         break
#     else:
#         print("Invalid choice :/")
#
import random


def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1


user = int(input("0 for snake, 1 for water, 2 for gun : "))
comp = random.randint(0, 2)
score = check(comp, user)
print("You : ", user)
print("Computer : ", comp)
if score == 0:
    print("Its a draw")
elif score == -1:
    print("You lose")
else:
    print("You won")

