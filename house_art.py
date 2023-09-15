<<<<<<< HEAD
#making a turtle portfolio program
#by Keith Jackson

import turtle

turtle.speed(0)
turtle.width(3)

def new_image(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def square(color, side):
    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(90)

def rectangle(color, side):
    l = 160
    w = 70
    for rectangle in range(4):
        if rectangle % 2 == 0:
            turtle.pencolor(color)
            turtle.forward(l)
            turtle.left(90)
        else:
            turtle.pencolor(color)
            turtle.forward(w)
            turtle.left(90)


def triangle(color, side):
    for triangle in range(3):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(120)

new_image(100, 0)
square('blue', 90)
new_image(-150, 0)
square('blue', 90)
new_image(-60, 0)
rectangle('green', 90)
new_image(-150, 90)
triangle('red', 90)
new_image(100, 90)
triangle('red', 90)


turtle.Screen().exitonclick()




=======
#making a turtle portfolio program
#by Keith Jackson

import turtle

turtle.speed(0)
turtle.width(3)

def new_image(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def square(color, side):
    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(90)

def rectangle(color, side):
    l = 160
    w = 70
    for rectangle in range(4):
        if rectangle % 2 == 0:
            turtle.pencolor(color)
            turtle.forward(l)
            turtle.left(90)
        else:
            turtle.pencolor(color)
            turtle.forward(w)
            turtle.left(90)


def triangle(color, side):
    for triangle in range(3):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(120)

new_image(100, 0)
square('blue', 90)
new_image(-150, 0)
square('blue', 90)
new_image(-60, 0)
rectangle('green', 90)
new_image(-150, 90)
triangle('red', 90)
new_image(100, 90)
triangle('red', 90)


turtle.Screen().exitonclick()




>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
