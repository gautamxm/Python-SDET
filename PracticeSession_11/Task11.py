import array
arr = array.array("i", [1,2,3,4,5])
n = int(input("enter a no : "))
rev1 = arr[:n]
rev2 = arr[n:]
print(rev2+rev1)
