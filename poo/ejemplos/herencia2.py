class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def saltar(self):
        print("saltando...")

    def comer(self):
        print("saltando...")



# clase Perro que hereda a la clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad, tipo, colorv):
        super().__init__(nombre, edad, tipo)
        self.color = colorv

    def ladrar(self):
        print("wau wau...")



# clase Gato que hereda a la clase Animal
class Gato(Animal):
    def __init__(self, nombre, edad, tipo, colav):
        super().__init__(nombre, edad, tipo)
        self.cola = colav

    def maullar(self):
        print("miau...")



perro1 = Perro("guffi", 2, "bulldog", "azul")
perro1.ladrar()


gato1 = Gato("wakanda", 3, "gato", "si")
gato1.maullar()



