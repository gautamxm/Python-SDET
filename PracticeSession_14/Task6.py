import math
class point:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2= y2
    def calc(self):
        print(math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2))
        
p1 = point(3,4,7,1)
p1.calc()