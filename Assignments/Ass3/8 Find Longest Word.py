# 8. Write a Python function to find the longest word in a given sentence.

str = input("Enter a String : ")
word = str.split()
longest = ""
for i in word:
    if len(longest) < len(i):
        longest = i
print(f"longest word {longest} of count : {len(longest)}")