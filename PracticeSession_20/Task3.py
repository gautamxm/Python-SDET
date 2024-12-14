from datetime import datetime
file = open("D:/BEBO/Python_SDET/Python-SDET/PracticeSession_20/example.txt","a")
curr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(curr)
file.write(curr)
# file.close()
print("all done")