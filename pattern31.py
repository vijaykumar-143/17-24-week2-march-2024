n=int(input("enter the number:\n"))
for i in range(1,n):
    for j in range(n,0,-1):
        if i<=j:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
