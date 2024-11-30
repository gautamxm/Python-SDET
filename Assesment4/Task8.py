dic = {
    "a" : 10,
    "b" : 10,
    "c" : 20,
    "d" : 10,
    "e" : 30,
}
list = []
for i,j in dic.items():
    if j == 10:
        list.append(i)

print(list)