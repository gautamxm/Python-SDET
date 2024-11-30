# 2. Count the frequency of characters in a string

str = input("Enter a Word : ")
occur = {}
for i in str:
    if i != " ":
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1

for i, count in occur.items():
    print(f"{i} : {count}")
