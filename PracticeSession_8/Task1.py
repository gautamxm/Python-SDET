# 1.	Find Common Values Between Two Dictionaries Using Sets 

mydic = {"a":2, "b":4, "c":6}
mydic2 = {"d":5, "e":4, "f":7}
myset = set([])
myset2 = set([])
for value in mydic.values():
    myset.add(value)
for value in mydic2.values():
    myset2.add(value)
print(myset & myset2)
