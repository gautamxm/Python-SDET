num1 = int(input("Enter first no. : "))
num2 = int(input("Enter second no. : "))

if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    print("Mixed Signal")
else: print("Same Signal")
