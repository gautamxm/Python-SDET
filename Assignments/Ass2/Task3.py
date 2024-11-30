# Leap Year Checker: Create a function that takes a year as input and determines if it's a leap year.

year = int(input("Enter a year to check if it's leap or not : "))
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} year is leap year")
else: print(f"{year} year is not leap year")
