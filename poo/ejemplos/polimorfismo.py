from abc import ABC, abstractmethod

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
 
    def sonido(self):
        pass


class Cotorro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido(self):
        print("pio pio")



cotorro1 = Cotorro("pablo")
cotorro1.sonido()
