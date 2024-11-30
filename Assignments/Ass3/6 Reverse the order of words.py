# 6. Write a Python program that reverses the order of words in a given sentence.


str = input("Enter a String : ")
words = str.split()
for i in words:
    print(i[::-1], end=" ")
