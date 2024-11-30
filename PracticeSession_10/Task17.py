# 17.	Implement a function to calculate the grade of a student based on marks in five subjects.

def grade(totalmarks):
    per = totalmarks/5
    if per > 90:
        return "Grade A+"
    elif per > 80:
        return "Grade A"
    elif per > 70:
        return "Grade B"
    else: return "Grade C"

h = int(input("enter your hindi marks out of 100 : "))
e = int(input("enter your english marks out of 100 : "))
m = int(input("enter your maths marks out of 100 : "))
s = int(input("enter your science marks out of 100 : "))
p = int(input("enter your punjabi marks out of 100 : "))
total = h+e+m+s+p
print(grade(total))