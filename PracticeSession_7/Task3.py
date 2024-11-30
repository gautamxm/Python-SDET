# Write a function called remove_duplicates that takes a list of integers and 
# returns a new list with duplicates removed while maintaining the original order.

# list1 = list(map(int, input("Enter the numbers : ").split()))
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)

# print(list2)

list = [1,1,2,3,3,4,5]
i = 0
while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] == list[j]:
            list.pop(j)
        else:
            j = j+1
    i+=1
    
print(list)