# Write a function called second_largest that takes a list of integers and 
# returns the second largest number

num = list(map(int, input("Enter the numbers : ").split()))
second = largest = num[0]

for num in num:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)