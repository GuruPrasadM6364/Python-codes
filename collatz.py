def collatz(a):
    if(a%2==0):
        print(a,"is even")
        b=a//2
        if b==1:
            return 1
        else:
            return 0
    else:
        print(a,"is odd")
        c=(3*a)+1
        return c
n=int(input("Enter the number:"))
m=collatz(n)
print(m)