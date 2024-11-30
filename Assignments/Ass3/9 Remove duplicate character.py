# Write a Python program to remove duplicate characters from a string while preserving the order of characters.

str = input("Enter a string : ")
unique = ""

for char in str:
    if char not in unique:
        unique += char

print("String after removing duplicates:", unique)
