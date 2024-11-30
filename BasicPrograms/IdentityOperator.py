x = [1,2,3,4]  # list
y = x
z = [1,2,3,4]

# IdentityOp references -- it stores the address of object
# is : check if two variable point to the same object in memory
# is not : check if two variable points to diff. objects

print(x is y)
print(x is z)
print(x is not y)
print(x is not z)

# diff bw is and ==
a = 5
b = 5
print(a == b)
print(a is b)
