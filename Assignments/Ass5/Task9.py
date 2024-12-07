# Write a list of integers, and use a lambda function with the filter function
# to filter out only the even numbers from the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Original list:", numbers)
print("Even numbers:", evenNumbers)