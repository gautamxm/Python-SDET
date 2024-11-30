maths = int(input("Enter Your Maths Marks out of 100 : "))
science = int(input("Enter Your Science Marks out of 100 : "))
totalAvg = int(input("Enter Your Total Average Marks out of 100 : "))

if (maths >= 80 and science >= 70) or totalAvg >= 75:
    print("You are eligible for admission")
else: print("You are not eligible")