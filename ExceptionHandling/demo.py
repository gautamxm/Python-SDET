
# print("this is starting of program")
# print("this is starting of program")
# print("this is starting of program")
# print("this is starting of program")
# arr=[1,2,3]
# try:
#     print(arr[8])
# # except:
# #     print("error occur")
# except Exception as e:
#     print(e)
# print("this is ending of program")
# print("this is ending of program")
# print("this is ending of program")

# num1,num2 = 10,20
# try:
#     result = num1/num2
#     print(result)
# except Exception as e:
#     print(e)
# else: print("no exception occur")
# finally: print("alll done")

# try:
#     print("Hello, world!")
# except:
#     print("Something went wrong")
# finally
#     print("This is the finally block")


# Raising our own Exception 
# def age(num):
#     if num < 0:
#         raise ValueError()
#     if num % 2 == 0:
#         print("even")
#     else: print("odd")

# num  =-1
# try:
#     age(num)
# except ValueError:
#     print("value error")
# print("all done")

# Custom Exception 
# class customError(Exception):
#     pass
# try:
#     raise customError("This is custom error msg")
# except Exception as e:
#     print(e)

# class NegativeNumberError(Exception):
#     def __init__(self,msg="-ve values are not allowed"):
#         self.msg = msg
#         super().__init__(self.msg)

# def checkPositive(number):
#     if number < 0:
#         raise NegativeNumberError("INVALID NUMBER, Please enter +ve number")
#     else: print(f"the number {number} is +ve")
 
# try:
#     num = int(input("enter a no: "))
#     checkPositive(num)
# except NegativeNumberError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
        
