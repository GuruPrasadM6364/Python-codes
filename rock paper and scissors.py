import random as ran 
n=ran.randint(0,3)
s=int(input("Enter the number of times to play:"))
for i in range(s):
    a=int(input("Enter a number 0(rock),1(paper),2(scissor) or any number to exit:"))
    if a==0:
        print("You chose rock")
        if n==1:
            print("I chose paper")
            print("I Won")
        elif n==2:
            print("I chose scissors")
            print("You Won")
        else:
            print ("I chose rock")
            print("No one won")
    elif a==1:
        print("You chose paper")
        if n==1:
            print("I chose paper")
            print("no one Won")
        elif n==2:
            print("I chose scissors")
            print("i Won")
        else:
            print ("I chose rock")
            print("you won")
    elif a==2:
        print("You chose scissors")
        if n==1:
            print("I chose paper")
            print("you Won")
        elif n==2:
            print("I chose scissors")
            print("no one Won")
        else:
            print ("I  chose rock")
            print("i won")