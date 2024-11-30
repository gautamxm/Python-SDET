# Write a function called to_title_case that converts a string to title case 
# (i.e., the first letter of each word should be uppercase).

str = input("Enter a string: ")
ans = ""
isFirst = True

for char in str:
    if char == " ":  
            ans += char
            isFirst = True
    elif isFirst:
        if 'a' <= char <= 'z':
            ans += chr(ord(char) - 32)
        else:
            ans += char
        isFirst = False
    else:
        if 'A' <= char <= 'Z':
            ans += char(ord(char) + 32)
        else:
            ans += char

print(ans)
