# 8.	Write a function describe_pet() that accepts an object and calls the speak() method on it.
# Create two classes, Parrot and Fish, where only the Parrot class has a speak() method.
# Pass objects of both classes to describe_pet() and observe the behavior.

def describe_pet(pet):
    pet.speak()

class Parrot:
    def speak(self):
        print("I'm a Parrot!")

class Fish:
    def speak(self):
        print("Fish can't speak")

parrot = Parrot()
fish = Fish()
describe_pet(parrot)
describe_pet(fish)
