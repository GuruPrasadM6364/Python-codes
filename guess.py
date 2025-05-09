import random as ran
n=ran.randint(1,101)
while True:
    a=int(input("Enter any number between 1 and 100:"))
    if a<n:
        print("Your guess is low")
        continue
    elif a>n:
        print("Your guess is high")
        continue
    else:
        print("You are correct")
        break
    