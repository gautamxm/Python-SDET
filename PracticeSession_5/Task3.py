str = input("Enter a String : ")
vowels = "aeiouAEIOU"
count = 0
for i in str:
    if i in vowels:
        count += 1
print(f"Number Vowels in {str} is : {count}")