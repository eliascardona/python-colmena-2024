from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
 
    @abstractmethod
    def sonido(self):
        print("Animal")


class Cotorro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido(self):
        print("pio pio")



cotorro1 = Cotorro("pablo")
cotorro1.sonido()
