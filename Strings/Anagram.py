s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
if len(s1) == len(s2):
    if(sorted(s1) == sorted(s2)):
        print("Its Anagram")
    else: print("Its Not anagram")