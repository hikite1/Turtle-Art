# Keith Jackson from Tonumoy Mukherjee


import turtle
import random
from turtle import *

turtle = Turtle()
wn = Screen()  # Screen Object
wn.bgcolor("black")  # Screen Bg color
wn.title("Fractal Tree Pattern")
turtle.left(90)  # moving the turtle 90 degrees towards left
turtle.speed(0)  # setting the speed of the turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.width(5)
colormode(255)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        turtle.pencolor('saddle brown')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        # turtle.pensize(1)
        turtle.backward(l)

draw(140)
turtle.right(30)
turtle._tracer(False)



# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        turtle.pencolor('saddle brown')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        # turtle.pensize(1)
        turtle.backward(l)


draw(140)
turtle.right(60)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        turtle.pencolor('saddle brown')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        # turtle.pensize(1)
        turtle.backward(l)


draw(140)
turtle.right(90)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        turtle.pencolor('saddle brown')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        # turtle.pensize(1)
        turtle.backward(l)


draw(140)
turtle.right(120)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        turtle.pencolor('saddle brown')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        # turtle.pensize(1)
        turtle.backward(l)


turtle._update()

wn.exitonclick()
