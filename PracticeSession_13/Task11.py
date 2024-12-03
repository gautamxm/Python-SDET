
class library:
    def __init__(self):
        self.books = []
    def addbook(self,bname):
        self.books.append(bname)
        print(f"{bname} added to library")
    def borrow(self,bname):
        if bname in self.books:
            self.books.remove(bname)
            print(f"you borrowed {bname} book ")
        else: print(f"{bname} not available")
    def display(self):
        print(self.books)

b = library()
b.addbook("its end with us")
b.addbook("its starts with us")
b.display()
b.borrow("its end with us")
b.display()
b.borrow("gautam")