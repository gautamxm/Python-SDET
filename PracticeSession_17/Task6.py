class parent:
    public = 10
    _protected = 100
    __private = 1000
    def m1(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

class child(parent):
    def m2(self):
        print(self.public)
        print(self._protected)
        # print(self.__private)  # private var cant accesssed

obj = child()
obj.m2()
