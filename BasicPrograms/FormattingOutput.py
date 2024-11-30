from math import remainder

name = "lucifer"
age = 21
salary = 50000

print("Name is :" ,name)
print("Age is :" ,age)
print("Salary is :" ,salary)

print("Name is : %s, Age is : %d, Salary is : %d" %(name,age,salary))

print("Name is : {}, Age is : {}, Salary is : {}".format(name,age,salary))

print(f"Name is : {name}, Age is : {age}, Salary is : {salary}") # F -  stand for formatted string

# addition of two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a + b
rem = a % b
print("Sum of two Numbers is", sum)
print("Remainder of two Numbers is", rem)


# TypeCasting
# Implicit - automatically performed by the interpreter
# Explicit - manual instruction programmer needs to give int(), float(), bool()