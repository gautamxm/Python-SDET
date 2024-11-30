# reverse the words in string 
str = input("Enter a String : ")
words = str.split()
for i in words:
    print(i[::-1], end=" ")
