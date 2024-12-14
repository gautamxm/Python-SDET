# file handling with text file 

# writing data in text file 
# open()
# file = open("D:/BEBO/Python_SDET/Python-SDET/FileHandling/gautam.txt","w")
# file.write("This is my first intstruction \n")
# file.write("This is my fourth intstruction \n")
# file.write("This is my third intstruction \n")
# file.write("This is my fourth intstruction \n")
# file.close()
# print("all done")

# reading data from text file 
# file = open("D:/BEBO/Python_SDET/Python-SDET/FileHandling/gautam.txt","r")
# print(file.read())
# print(file.readline())
# print(file.readable())
# file.close()

# appending data nto text file 
# file = open("D:/BEBO/Python_SDET/Python-SDET/FileHandling/gautam.txt","a")
# file.write("This is my fifth intstruction \n")
# file.write("This is my sixth intstruction \n")
# file.write("This is my seventh intstruction \n")
# file.close()
# print("all done")

# remove the file 
# import os
# try:
#     os.remove("D:/BEBO/Python_SDET/Python-SDET/FileHandling/gautam.txt")
#     print("file removed")
# except Exception as e:
#     print(e)

# os.rmdir("path of file")