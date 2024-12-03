
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"Brand : {self.brand}, Model : {self.model}"
    
obj = car("tata","nexon")
del obj.brand
print(obj)
