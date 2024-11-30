# 1. Check if a string is a palindrome.

s = input("Enter a String : ")
rev = ""
for i in s:
    rev = i + rev
if s == rev:
    print("Given string is palindrome")
else: print("Given string is not palindrome")