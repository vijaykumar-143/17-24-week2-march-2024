n=int(input("enter the number: \n"))
for i in range(1,n+1):
    x=64
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(x+k),end=" ")
    print()
