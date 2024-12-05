class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def startengine(self):
        print(f"{self.model} Engine is starting of model {self.year}")

car1 = car(f"TATA", "NEXON", 2020)
car1.startengine()

car2 = car(f"HYUNDAI", "CRETA", 2023)
car2.startengine()
