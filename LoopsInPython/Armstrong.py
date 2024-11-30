n = int(input("Enter a no. : "))
temp = n
sum = 0
power = len(str(n))

while temp > 0:
    lastDigit = temp % 10
    sum += lastDigit ** power
    temp = temp // 10

if n == sum:
    print(f"{n} is armstrong number")
else: print(f"{n} is not a armstrong number")

