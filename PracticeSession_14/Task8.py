class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def discount(self,discount):
        self.price -= discount/100 * self.price
    def display(self):
        print(f"{self.name} : {self.price}")

p1 = product("phone",20000)
p2 = product("light",2000)
p3 = product("tv",30000)
p1.display()
p2.display()
p3.display()
p1.discount(20)
p1.display()