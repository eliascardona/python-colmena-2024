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


#  EJERCICIO CUADRADO MAGICO
bob.hideturtle()
bob.penup()
x_current = -200
y_current = -200


bob.setposition(-300, -200)
for i in range(0, 200):
    bob.fd(20)
    bob.dot(20, color_gen())
    x_current += 50
    bob.setposition(x_current, y_current)

    current_position = bob.position()
    if(current_position[0] == 200):
        y_current += 50
        bob.setposition(x_current, y_current)
        bob.backward(20)