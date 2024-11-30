n = int(input("enter a no. : "))
a = 0
b = 1
# print(a)
# print(b)
for i in range(2,n):
    fib = a + b
    # print(fib)
    a,b = b,fib
print(fib)