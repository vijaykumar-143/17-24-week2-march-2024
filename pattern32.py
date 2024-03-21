n=int(input("enter the number :\n"))
x=64
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(chr(x+i+j-1),end=" ")
    print()
