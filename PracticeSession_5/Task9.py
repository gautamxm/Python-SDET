# occurence of alphabet in words 
word = input("Enter a Word : ")
occur = {}
for i in word:
    if i != " ":
        if i in occur:  
            occur[i] += 1
        else: occur[i] = 1
    

for i,count in occur.items():
    print(f"{i} : {count}")