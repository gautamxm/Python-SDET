n = int(input("Enter a no. : "))

# * * *
# * * *
# * * *
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")   # end is using for horizontal printing
#     print()  # for new line


# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ") 
#     print()  


# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(n):
#     for j in range(i,n):
#         print("*", end=" ") 
#     print()


#       * 
#     * * 
#   * * *
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


# * * *
#   * *
#     *
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print("*", end=" ")
#     print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     for l in range(n-i-1):
#         print(" ",end=" ")
#     print()


# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2*n - (2*i + 1)):
#         print("*",end=" ")
#     for l in range(i):
#         print(" ",end=" ")
#     print()


#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for k in range(2*i + 1):
#         print("*", end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for k in range(2*i + 1):
#         print("*", end=" ")
#     print()


# 1
# 1 2
# 1 2 3
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

number = 1
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print(number,end=" ")
        number+=1
    print()