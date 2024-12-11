
mydic = {
    "apple": 90,
    "mango" : 80,
    "banana" : 70,
    "cherry" : 70
}

name = input("enter fruits name : ")
try:
    print(mydic[name])
except KeyError:
    print(f"{name} is not in dict")