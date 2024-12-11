
num = int(input("enter a no : "))
try:
    if num > 0:
        print(num**2)
    else: raise ValueError("-ve value not allowed")
except Exception as e:
    print(e)


