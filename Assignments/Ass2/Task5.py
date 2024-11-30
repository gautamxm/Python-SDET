# Sum of Even Numbers: Create a program that accepts a positive integer n and calculates the sum of all even numbers from 1 to n. For example, if n is 10, the output should be 30 (2 + 4 + 6 + 8 + 10).

num = int(input("Enter a +ve number : "))
sum = 0
for i in range(0,num+1,2):
    sum += i
print(sum)