str = input("Enter a String : ")
word = ""
# word = str.replace(" ", "")
for char in str:
    if char != " ":
        word += char
print("String without spaces is : ", word)