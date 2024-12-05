class laptop:
    def __init__(self,branch,model):
        self.name = branch
        self.model = model
    def specs(self):
        print(f"Laptop of company : {self.name}, and model is {self.model}")

l1 = laptop("HP", "EliteBook")
l2 = laptop("ASUS", "VivoBook")
l1.specs()
l2.specs()
        