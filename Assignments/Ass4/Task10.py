# Write a Python function that checks whether a given key exists in a dictionary. If the key is present,
# return its value; otherwise, return 'Key not found'.

def check(mydict,elm):
    for key,value in mydict.items():
        if key == elm:
            return  value
    else: return  "key not found"
mydict = {"a" : 4, "b" : 6, "c" : 10, "d" : 8, "e" : 5 }
gkey = "c"
res = check(mydict,gkey)
print(f"given key {gkey} and its value is {res}")

