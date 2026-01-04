import random

num=random.randint(1,5)
guess= int(input("Guess a number between 1 to 5:"))

if guess==num:
    print("Correct Guess!!")
else:
    print("Wrong Guess!Number was",num)
    