# Write a Counter class with a class variable count to keep track of how many objects have been created.
# Test this by creating multiple objects and printing the count

class counter:
    count = 0
    def fun(self):
        counter.count += 1
        print(counter.count)
obj1 = counter()
obj1.fun()   # 1
obj2 = counter()
obj2.fun()  # 2
obj3 = counter()
obj3.fun()  # 3