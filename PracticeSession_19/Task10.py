
try:
    n=int(input("Enter the number"))
    print(n/0)
except Exception as e:
    print(e)
finally:
    print("---The End---")