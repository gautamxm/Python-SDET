# 7.	Create a function to check whether a given string is a palindrome.

def palindrome(str):
    rev = ""
    for i in str:
        rev = i + rev
    if str == rev:
        print("given string is palindrome")
    else: print("given string is not palindrome")
str = input("enter a string : ")
palindrome(str)