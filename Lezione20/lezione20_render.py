from abc import ABC, abstractmethod
class Forma(ABC):
    def __init__(self,nome):
        self.nome=nome
    @abstractmethod
    def getArea(self):
        pass
    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self,lato):
        super().__init__("Quadrato")
        self.lato=lato
    
    def getArea(self):
        return self.lato*self.lato
    
    def render(self):
        for i in range(self.lato):
            print("*", end=" ")
        print()
        for r in range(self.lato-2):
            print("*", end=" ")
            for c in range(self.lato-2):
                print(" ", end=" ")
            print("*")
        for i in range(self.lato):
            print("*", end=" ")

q=Quadrato(4)
print(q.getArea())
q.render()

class Rettangolo(Forma):
    def __init__(self,base,altezza):
        super().__init__("Rettangolo")
        self.base=base
        self.altezza=altezza
    
    def getArea(self):
        return self.base*self.altezza
    
    def render(self):
        a=0
        for i in range(self.base):
            print("*", end=" ")
        print()
        for r in range(self.altezza-2):
            print("*", end=" ")
            for c in range(self.base-2):
                print(" ", end=" ")
            print("*")
        for i in range(self.base):
            print("*", end=" ")


r=Rettangolo(7,5)
print()
print(r.getArea())
r.render()
print()
