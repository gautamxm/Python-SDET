# Write a Python function that sorts a list of strings based on the length of the strings

def sortlist(strlist):
    return sorted(strlist, key=len)

list = ["apple", "kiwi", "mangoo", "pomegranate", "watermelon"]
res = sortlist(list)
print(res)

