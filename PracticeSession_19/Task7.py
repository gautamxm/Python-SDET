
class InvalidAgeException(Exception):
    def __init__(self,msg="age shouldn't be less than 18"):
        self.msg = msg
        super().__init__(self.msg)

def checkAge(age):
    if age < 18:
        raise InvalidAgeException()
    else: print(f"Your age is {age}")

try:
    age = int(input("enter age : "))
    checkAge(age)
except Exception as e:
    print(e)