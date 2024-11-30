# Write a Python program to count the occurrences of each word in a given sentence.

str = input("Enter a string : ")
wordcounts = {}
words = str.split()

for i in words:
    if i in wordcounts:
        wordcounts[i] += 1
    else:
        wordcounts[i] = 1

for word, count in wordcounts.items():
    print(f"'{word}': {count}")