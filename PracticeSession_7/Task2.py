# Write a function called sum_of_digits that takes an integer and returns the sum of its digits. 
# Use arithmetic operators to extract the digits

n = int(input("Enter a no : "))
sum = 0
while n > 0:
    last = n % 10
    sum += last
    n = n // 10
print(sum)


