n=int(input("enter the number: \n"))
x=2
for i in range(0,n):
    for j in range(1,n+1):
        if(j>=(n-i)):
            print(x,end="  ")
            x=x+2
        else:
            print("  ",end="  ")
    print()
