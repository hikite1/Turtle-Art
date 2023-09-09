#Keith Jackson from Tonumoy Mukherjee


import turtle
import random
from turtle import *

turtle = Turtle()
wn = Screen() #Screen Object
wn.bgcolor("black") #Screen Bg color
wn.title("Fractal Tree Pattern")
turtle.left(90) #moving the turtle 90 degrees towards left
turtle.speed(0)#setting the speed of the turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.width(5)
colormode(255)


def draw(l): #recursive function taking length 'l' as argument
    if(l<10):
        return
    else:

        turtle.pensize(2) #Setting Pensize
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l) #moving turtle forward by 'l'
        turtle.left(30) #moving the turtle 30 degrees towards left
        draw(3*l/4) #drawing a fractal on the left of the turtle object 'turtle' with 3/4th of its length
        turtle.right(60) #moving the turtle 60 degrees towards right
        draw(3*l/4) #drawing a fractal on the right of the turtle object 'turtle' with 3/4th of its length
        turtle.left(30) #moving the turtle 30 degrees towards left
        turtle.pensize(2)
        turtle.backward(l) #returning the turtle back to its original psition

draw (20) # drawing 20 times 

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(3*l/4)
        turtle.right(60)
        draw(3*l/4)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)

draw (20)

turtle.left(270)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(3*l/4)
        turtle.right(60)
        draw(3*l/4)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)

draw (20)

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(3*l/4)
        turtle.right(60)
        draw(3*l/4)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)

draw(20)

turtle.right(90)

def draw(l):
    if(l<10):
        return
    else:

        turtle.pensize(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(4*l/5)
        turtle.right(60)
        draw(4*l/5)
        turtle.left(30)
        turtle.pensize(3)
        turtle.backward(l)

draw (40)

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(4*l/5)
        turtle.right(60)
        draw(4*l/5)
        turtle.left(30)
        turtle.pensize(3)
        turtle.backward(l)

draw (40)

turtle.left(270)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(4*l/5)
        turtle.right(60)
        draw(4*l/5)
        turtle.left(30)
        turtle.pensize(3)
        turtle.backward(l)

draw (40)

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(4*l/5)
        turtle.right(60)
        draw(4*l/5)
        turtle.left(30)
        turtle.pensize(3)
        turtle.backward(l)

draw (40)

turtle.right(90)

turtle._tracer(False)

def draw(l):
    if(l<10):
        return
    else:
        
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(6*l/7)
        turtle.right(60)
        draw(6*l/7)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)
        
draw (60)

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(6*l/7)
        turtle.right(60)
        draw(6*l/7)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)
        
draw (60)

turtle.left(270)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(6*l/7)
        turtle.right(60)
        draw(6*l/7)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)
        
draw (60)

turtle.right(90)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        turtle.pensize(2)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
        draw(6*l/7)
        turtle.right(60)
        draw(6*l/7)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)
draw(60)
turtle._update()

wn.exitonclick()
