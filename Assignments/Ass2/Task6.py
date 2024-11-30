# 6.	Sum of Digits Until Single Digit: Create a function that takes an integer as input and repeatedly finds the sum of its digits until a single-digit number is obtained. For example, if the input is 9875, the output should be 2 (9+8+7+5=29 -> 2+9=11 -> 1+1=2).

n = int(input("Enter a digit : "))
while n >= 10:
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n //= 10
    n = sum
print(f"Single digit sum is : {sum}")

