n=int(input("enter the number:\n"))
for i in range(1, n+1):
        for j in range(1, i+1):
            if j == i:
                print(i - 1, end=" ")
            else:
                print(j - 1, end=" ")
        print()
