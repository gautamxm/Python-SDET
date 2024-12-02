
class book:
    def bookinfo(self,title,author="unknown"):
        print(title,author)

obj1 = book()
obj2 = book()

obj1.bookinfo("pirates of grill","lucifer")
obj2.bookinfo("its end with us")