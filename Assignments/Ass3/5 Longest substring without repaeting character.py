# 5. Longest substring without repeating characters

str = input("Enter a string : ")
characterList = []
longest = 0

for char in str:
    if char in characterList:
        while char in characterList:
            characterList.pop(0)
    characterList.append(char)
    longest = max(longest, len(characterList))

print("Length of the longest substring without repeating characters:", longest)