# i = 1
# while i <= 10:
#     print(i)
#     i+= 1
# print("Done")

# i = 10
# while i >= 1:
#     print(i)
#     i-= 1
# print("Done")

# to print 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i+= 1
# print("Done")

# sum of first n natural no.
# num = int(input("Enter the no. : "))
# i = 1
# sum = 0
# while i <= num:
#     sum = sum + i
#     i = i+1
# print(sum)

# factorial of no.
# num = int(input("Enter the no. : "))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact * i
#     i = i+1
# print(fact)

#reverse of no.
# num = int(input("Enter the no. : "))
# rev = 0
# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# print(rev)

# count the no. of digit
num = int(input("Enter the no. : "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print(count)

