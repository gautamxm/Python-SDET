
from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def m1(self):
        print("hello")

obj = parent()
obj.m1()

# TypeError: Can't instantiate abstract class parent without an implementation for abstract method 'm1'
