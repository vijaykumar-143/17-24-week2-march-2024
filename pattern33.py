n=int(input("enter the number :\n"))
x=64
for i in range(n):
    for j in range(0,n-i):
        print(chr(x+j+1),end=" ")
    print()
