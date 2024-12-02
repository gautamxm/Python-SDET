
class library:
    totalbooks = 0
    def newbook(self,new):
        self.totalbooks += new
        print(self.totalbooks)
mc = library()

mc.newbook(5)
mc.newbook(5)