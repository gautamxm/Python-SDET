# 7.	Login Authentication: Write a program that accepts a username and password from the user and checks if they match the pre-set username and password. If both match, print "Access Granted"; otherwise, print "Access Denied."

user = input("Enter your username : ")
pasw = input("Enter your password : ")

if user == "admin123" and pasw == "12345":
    print("Access Granted")
else: print("Access Denied")