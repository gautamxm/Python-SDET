# replace alphabet in word 
word = input("enter a string : ")
oldchar = input("enter a alphabet to replace : ")
newchar = input("enter new alphabet to replace : ")
new = ""
for i in word:
    if i == oldchar:
        i = newchar
        new += i
    else: new += i
print(new)

