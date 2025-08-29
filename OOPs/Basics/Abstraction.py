from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def Milege(self):
        pass

class Audi(Car):
    def Milege(self):
        print("20kmpl")

class BMW(Car):
    def Milege(self):
        print("10kmpl")

c1 = Audi()
c1.Milege()
