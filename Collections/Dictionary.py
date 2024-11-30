# Dictionary - key,value pair
# - ordered, changeable and indexed {}
# Keys - must be unique, must be immutables
# Values - can be of any type 

# Creating dict 
# mydic = {"name" : "bob", "age" : 23, "address" : "India"}
# print(mydic)

# Using list of tuples --dict()
# List not possible beacuse its mutable
# mydic = dict([("name","bob"),("age",23),("address","India")])
# print(mydic)

# using dict() constructor
# mydic = dict(name="bob",age=23)
# print(mydic)

# Accessing the elements of dic 
# mydic = {"name":"bob", "age":23, "address": "India"}
# print(mydic["name"])
# print(mydic["address"])
# print(mydic["dept"])    # KeyError: 'dept'

# using get() method
# mydic = {"name":"bob", "age":23, "address": "India"}
# print(mydic.get("name"))
# print(mydic.get("age"))

# Modifying the dic 
# - Adding or update key value pair 
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# print(mydic["age"])
# mydic["age"] = 25
# print(mydic["age"])
# mydic["city"] = "Ambala"
# print(mydic)

# Deleting a key value pair 
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# del mydic["address"]
# print(mydic)

# pop() -- going to delete specific item
# mydic.pop("age")

# popitem() 
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# mydic["city"] = "ambala"
# print(mydic)
# mydic.popitem() -- remove the last item

# clear() -- delete all items from dic 
# mydic.clear()

# DICTIONARY METHODS 
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# keys() methods - return the object of keys in set
# print(mydic.keys())

# value() - return value 
# print(mydic.values())

# items() - return both key n value in tuple form 
# print(mydic.items())

# update() - to insert multiple values
# update dic with diff set of key n value from another dic 
# mydic1 = {"name":"Gautam", "age":23, "address": "India"}
# mydic2 = {"city":"heyy", "location":"jamnapar"}
# mydic1.update(mydic2)
# print(mydic1)

# copy() - return the copy of dictionary 
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# mydic1 = mydic.copy()
# print(mydic1)

# fromKeys() - create copy of dic with specified key n a single value 
# keys = [1,2,3]
# defaultVal = "welcome"
# mydic = dict.fromkeys(keys,defaultVal)
# print(mydic)

# setDefault() - return the value of a key if its in the dic 
# if not, it inserts the key with specified default value 
# mydic = {"name":"Gautam", "address": "India"}
# mydic.setdefault("age",30)
# print(mydic)

# Iteratory over dic 
# Using for Loop
# mydic = {"name":"Gautam", "age":23, "address": "India"}
# for key in mydic:
#     print(key)

# Iterating over values
# for value in mydic.values():
#     print(value)

# iterate over both key n value 
# for key,value in mydic.items():
#     print(key,value)

# Dictionary comprehension 
# {0:0,1:1,2:4,3:9}
# square = {x: x**2 for x in range(0,11)}
# print(square)

# Nested Dictionary
# mydic = {
#     "p1" : {"name":"gautam", "age":23},
#     "p2" : {"name":"lucifer", "age":25},
# }
# print(mydic["p1"]["name"])
# print(mydic["p2"]["age"])

# Merging Dictionary using union operator
# dic1 = {"A":1,"B":2,"C":3}
# dic2 = {"A":1,"E":2,"F":3}

# returning commom values from dic 
# mydic1 = {"name":"gautam", "age":23}
# mydic2 = {"name":"gautam", "age":25}
# l1 = set(mydic1.values())
# l2 = set(mydic2.values())
# l3 = l1.intersection(l2)
# print(l3)

# mydic = {"name":"gautam", "age":23}
# keys = set(mydic.keys())
# print(keys)

# mydic = {"a":10, "b":23, "c":10, "d":23, "e":15}
# val = set(mydic.values())
# print(val)

# mydic = {"name":"gautam", "age":23}
# serch = {"age" : 23}
# if mydic["age"] == 23:
#     print("True")
# else : print("False")
