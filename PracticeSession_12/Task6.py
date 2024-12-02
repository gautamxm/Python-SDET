
class calc:
    def add(self,a,b):
        print(a+b)
    @staticmethod
    def info():
        print("this is calculator class")

obj = calc()
obj.add(3,5)
calc.info()