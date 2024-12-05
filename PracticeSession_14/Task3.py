class counter:
    count = 0
    def __init__(self):
        counter.count += 1
        print(self.count)

a = counter()
b = counter()
c = counter()
