# 3.	Write a class Calculator with a method add() that can handle two or three arguments.
# Use default arguments to achieve method overloading behavior.

class calculator:
    def add(self,a,b,c=0):
        return a+b+c

t1 = calculator()
print(t1.add(5,5))   # 10
print(t1.add(5,5,10))  # 20 
