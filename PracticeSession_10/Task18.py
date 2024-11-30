# 18.	Write a function that takes a string and returns a dictionary with the frequency of each word in the string.

def freq(str):
    mydic = {}
    words = str.split()
    for word in words:
        if word not in mydic:
            mydic[word] = 1
        else: mydic[word] += 1
    return mydic

strring = "hey there hey learning python learning"
print(freq(strring))

