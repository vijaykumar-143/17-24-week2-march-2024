n=int(input("enter the number:\n"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
