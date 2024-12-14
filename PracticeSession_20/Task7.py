
name = input("enter name of file : ")
file = open(f"D:/BEBO/Python_SDET/Python-SDET/PracticeSession_20/{name}","r")

lines = file.readlines()

num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_characters = sum(len(line) for line in lines)

print(f"Number of Lines: {num_lines}")
print(f"Number of Words: {num_words}")
print(f"Number of Characters: {num_characters}")