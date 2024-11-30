# 2.	Create a Dictionary and Convert Its Keys to a Set

mydic = {"a":2, "b":4, "c":6}
myset = set([])
for key in mydic.keys():
    myset.add(key)
print(myset)