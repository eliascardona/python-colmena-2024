from turtle import Turtle,Screen
import random

bob = Turtle()
#ATRIBUTOS PANTALLA
screen = Screen()
screen.colormode(255)
#ATRIBUTOS TORTUGA
bob.shape("turtle")
bob.color("red")

def color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors  = (r, g, b)
    return colors


#  MODIFICAR MANUALMENTE LA POSICION DE TORTUGA





