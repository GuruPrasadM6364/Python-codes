def zig():
    i=0
    x=int(input("enter the number of rows"))
    for i in range (x):
        while i<=x-2:
            space=' '
            i+=1
            space*=i
            print(space+'$'*5)
        i-=1
        while i>0:
            space=' '
            space*=i
            print(space+'$'*5)
            i=i-1
        break
user=input("enter s for start and p for stop")
while True:
    if user=='s':
        zig()
    else:
        break
 