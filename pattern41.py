n=int(input("enter the number: \n"))
x=65
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(x),end=" ")
    x=x+1
    print()
