
class product:
    def __init__(self,price,stock):
        self.__price = price
        self.__stock = stock

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,newPrice):
        if newPrice > 0:
            self.__price = newPrice
        else:
            print("Price cant be -ve")
    
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,newStock):
        if newStock > 0:
            self.__stock = newStock
        else:
            print("stock cant be -ve")

obj = product(9000,10)
print(obj.price)
print(obj.stock)
obj.price = -89
obj.stock = 100
print(obj.price)
print(obj.stock)