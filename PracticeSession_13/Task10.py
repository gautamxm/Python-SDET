
class shoppingcart:
    def __init__(self):
        self.list = []
    def additem(self,itemname):
        self.list.append(itemname)
        print(f"Item : {itemname} added to the cart")
    def removeitem(self,itemname):
        if itemname in self.list:
            self.list.remove(itemname)
            print(f"Removed {itemname} from the cart")
        else: print(f"{itemname} is not in the cart")
    def display(self):
        print(self.list)

obj = shoppingcart()
obj.additem("apple")
obj.additem("mango")
obj.display()
obj.removeitem("apple")
obj.display()

        