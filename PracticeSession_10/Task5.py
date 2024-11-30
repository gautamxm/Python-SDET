def pattern(num):
    for i in range(1,num+1):
        for j in range(i):
            print("*", end=" ")
        print()
num = int(input("enter a no. : "))
pattern(num)