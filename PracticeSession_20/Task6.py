
file1 = open("D:/BEBO/Python_SDET/Python-SDET/PracticeSession_20/example.txt","r")
content = file1.read()
file2 = open("D:/BEBO/Python_SDET/Python-SDET/PracticeSession_20/destination.txt","w")
file2.write(content)
print("all done")