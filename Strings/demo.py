# creating strings
# s = 'welcome'
# s = "welcome"
# s = str("welcome")
# s = str('welcome')

# creating empty string
# name = ''
# name = ""
# name = str()

# strings are immutable
# name = "lucifer"
# print(name)
# name[0] = "k"
# print(name)   # will throw typeError

# message = "Welcome"
# print(id(message))
# message = message + "Home"
# print(id(message))

# + and * with string
# str = "welcome"
# print(str + "python")
# print(str*2)

# Slicing in string 
# str = "welcome"
# print(str[1:3])
# print(str[:3])
# print(str[2:])
# print(str[1:-1])  # last one character will be removed
# print(str[1:-2])  # last two character will be removed
# print(str[-4:-1])

# ord() and chr() method
# print(ord("A"))
# print(ord("a"))
# print(chr(65))
# print(chr(97))

# max(), min(), len()
# print(max("abc"))
# print(max("def"))
# print(min("qrs"))
# print(min("hdj"))
# print(len("lucifer"))
# print(len("lucifer  "))

# in, not in operators
# s = "welcome"
# print("come" in s)
# print("come" not in s)
# print("lome" in s)
# print("lome" not in s)

# string comparison
# print("tim" == "tie")   -false
# print("free" != "freedom")   -true
# print("arrow" > "aron")   -true
# print("right" >= "left")   -true
# print("teeth" <= "tee")   -false
# print("yellow" <= "fellow")    -false
# print("abc" > "")     -true


# Testing Strings
# s = "welcome to python" 
# print(s.isalnum())   #--check both alphabets n numerics
# print("welcome to python".isalpha())  #--false -its checks string contain only alphabets not space
# print("welcometopython".isalpha())  #--true

# print("2022".isdigit())  

# print(s.isidentifier())
# print("if".isidentifier())

# print(s.islower())
# print("WELCOME".isupper())
# print("  ".isspace())


# Searching In Strings
# s = "welcome to python"
# print(s.endswith("thon"))
# print(s.startswith("wel"))

# print(s.find("come"))
# print("hcome".find("hello"))

# print(s.count("o"))  # return no of occurence in the string
# print(s.count(" "))

# Converting Strings
# s = "string in python"

# print(s.capitalize())  #String in python
# print(s.title())  #String In Python
# print("WELCOME".lower())  #welcome
# print(s.upper())  #STRING IN PYTHON
# print(s.swapcase())  #STRING IN PYTHON
# print("HELLO".swapcase())  #hello
# print(s.replace("in", "on"))  #strong on python
# print(s.replace("py", "on"))  #string in onthon


# Reversing in Strings

# s = "welcome"
# revStr = ""
# for i in s:
#     revStr = i+revStr
# print(revStr)

# revStr = s[::-1]
# print(revStr)

# count the no. of vowels and words 
# remove all the spaces from string
# program to convert string into uppercase
# implement the concept of tuple