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

# for i in range(100):
#     bob.color(color_gen()) 
# bob.forward(100)
# bob.left(90)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         bob.color(c)
#         bob.forward(steps)
#         bob.right(30)

# for figuras in range(100):
#     for color in ('blue', 'red', 'green'):
#         bob.forward(100)
#         bob.right(angulo/numero_de_lados)
#     numero_de_lados+=1
#     bob.color(color_gen())

# bob.speed(0)
# for grado in range(0, 361, 25):
#     bob.color(color_gen())
#     bob.shearfactor(grado)
#     bob.circle(60)


# print(bob.position())
# bob.fd(100)
# bob.right(90)
# bob.fd(50)
# print(bob.position())

# bob.setpos(35, -100)
# bob.penup()
# bob.fd(100)
# bob.right(90)
# bob.fd(50)

# bob.hideturtle()
# for i in range(5):
#     bob.forward(100)
#     bob.dot(5, color_gen())

bob.hideturtle()
bob.penup()
bob.setpos(-200, -150)
x_limit = 200
y_current_step = 0
# y_step_length = 10


for j in range(0, 5, 1):
    for i in range(0, 200, 10):
        bob.forward(20)
        bob.dot(20, color_gen())
        current_position = bob.position()

    if(current_position[0] == x_limit):
        y_current_step += 10
        bob.setposition(x_limit, y_current_step)
        # bob.right(90)
        bob.forward(1)




screen.exitonclick()