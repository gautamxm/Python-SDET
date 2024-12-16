# Create a class Grandparent with a method say_hello(). Inherit this class into Parent, and then into Child.
# Demonstrate how the Child class can access methods from Grandparent and Parent.

class Grandparent:
    def say_hello(self):
        print("Hello from Grandparent!")

class Parent(Grandparent):
    def say_hello(self):
        print("Hello from Parent!")

class Child(Parent):
    def say_hello(self):
        Grandparent.say_hello(self)
        Parent.say_hello(self)
        print("Hello from Child!")

child = Child()
child.say_hello()

