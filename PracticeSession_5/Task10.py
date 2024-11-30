# to print the longest word with its length 
str = input("Enter a String : ")
word = str.split()
longest = ""
for i in word:
    if len(longest) < len(i):
        longest = i
print(f"longest word {longest} of count : {len(longest)}")