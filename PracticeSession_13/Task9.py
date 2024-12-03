
class bankaccount:
    def __init__(self,balance):
        self.bal = balance
    def deposit(self, amount):
        self.bal += amount
        print(f"Current Amount : {self.bal}")
    def withdrawn(self, amount):
        if amount > 0 and amount <= self.bal:
            self.bal -= amount
        print(f"Withdrawn : {amount}, Updated Amount : {self.bal}")
    def checkbal(self):
        print(f"Balance Amount : {self.bal}")

obj = bankaccount(1000)
obj.deposit(1000)
obj.withdrawn(500)
obj.checkbal()

    
    
        