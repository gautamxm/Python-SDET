
class animal:
    def makesound(self,sound="default"):
        print(sound)

class dog(animal):
    def makesound(self,sound="baba"):
        print(sound)

class cat(animal):
    def makesound(self,sound="meow"):
        print(sound)

class cow(animal):
    def makesound(self,sound="gaaa"):
        print(sound)

obj1 = cow()
obj1.makesound()

obj2 = dog()
obj2.makesound()

obj3 = cow()
obj3.makesound()