str = input("Enter a String : ")
count = 0
word = ""

for char in str:
    if char != " ":
        word += char
    else:
        count += 1
        word = ""

if word:
    count += 1

print("Number of Words in Given String are : ", count)
