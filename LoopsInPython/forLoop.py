# for i in range(1,11):
#     print(i)

# sum of number from 1 to 100
# sum = 0
# for i in range(1, 101):
#     sum = sum + i 
# print(f"sum of no. from 1 to 100  : {sum}")

# sum of n natural no using for loop
# num = int(input("Enter the no : "))
# sum = 0
# for i in range(1, num+1):
#     sum = sum + i
# print(sum)

# even no. 1 to 20
# for i in range(1, 21):
#     if(i % 2 == 0):
#         print(i)

# factorial of no.
# num = int(input("Enter the no : "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(fact)

# multiplication table
# num = int(input("Enter the no : "))
# for i in range(1, 11):
#     ans = num * i
#     print(f"{num} * {i} = {ans}")

# to check no. is prime or not
num = int(input("Enter the no : "))
prime = True
for i in range(2, num):
    if(num % i == 0):
        prime = False
        break

if prime:
    print("its is prime")
else:
    print("not prime")