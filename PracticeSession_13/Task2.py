
class book:
    def __init__(self,bname,bauthor):
        self.bname = bname
        self.bauthor = bauthor
    def __str__(self):
        return f"Book Name : {self.bname}, Author : {self.bauthor}"
    
obj = book("its end with us","coolen hover")
print(obj)
        