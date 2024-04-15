import time
timestamp = time.strftime('The time right now : %H:%M:%S')
print(timestamp)

# print("The time right now is : ", timestamp)
# hour = int(time.strftime('%H'))

hour = int(input("Enter the time : "))

print(hour)

# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)

if (hour >= 0 and hour < 12):
    print("Good Morning Sir!")
elif (hour >= 12 and hour < 17):
    print("Good Afternoon Sir!")
if (hour >= 17 and hour < 0):
     print("Good Night Sir!")
