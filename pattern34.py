n=int(input("enter the number :\n"))
x=65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(x),end=" ")
        x=x+1
    print()
