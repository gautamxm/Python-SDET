# 9.	Ride Height Requirement: Youâ€™re managing a theme park ride. To go on the ride, a person must be at least 48 inches tall. However, if theyâ€™re between 42 and 47 inches, they can ride if accompanied by an adult. If they are under 42 inches, they cannot ride at all. Write a function that takes in the height and a boolean for whether an adult is present, and returns True if they can ride, False otherwise.

def can_ride(height, adult_present):
    if height >= 48:
        return True
    elif 42 <= height <= 47 and adult_present == "yes":
        return True
    else:
        return False

height = int(input("Enter the person's height in inches: "))
adult_present = input("Is an adult present? (yes/no): ")

if can_ride(height, adult_present):
    print("The person can ride.")
else:
    print("The person cannot ride.")