

class Animal:
    def sound(self):
        print("Base class")

class Dog(Animal):
    def sound(self):
        return "baau baau"

class Cat(Animal):
    def sound(self):
        return "meoww meoww"

class Cow(Animal):
    def sound(self):
        return "gaaaa"

def play_sound(animal):
    print(animal.sound())

dog = Dog()
play_sound(dog) 
cat = Cat()
play_sound(cat)  
cow = Cow()
play_sound(cow)  

