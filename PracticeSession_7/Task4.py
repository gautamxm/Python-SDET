# Write a function called min_max_tuple that takes a tuple of integers and 
# returns a tuple containing the minimum and maximum values from the input tuple.

tuple = tuple(map(int, input("Enter the numbers : ").split()))
min = tuple[0]
max = tuple[0]
for i in tuple:
    if i < min:
        min = i
    if i > max:
        max = i

res = (min,max)
print(f"minimum and maximum values are : {res}")