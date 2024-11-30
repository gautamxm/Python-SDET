s = input("Enter a String : ")
rev = s[::-1]
if s == rev:
    print("its palindrome")
else: print("its not palindrome")

rev = ""
for i in s:
    rev = i + rev
if s == rev:
    print("its palindrome")
else: print("its not palindrome")