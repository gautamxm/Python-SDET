age = int(input("Enter Your Age : "))
dl = input("Have License? ")

if age >= 18 and dl == "yes":
    print("You are eligible to drive")
else: print("You are not eligible")