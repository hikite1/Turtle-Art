<<<<<<< HEAD
import turtle

turtle.speed(0)
turtle.width(3)


def new_image(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(color, side):
    l = 170
    w = 50
    for rectangle in range(4):
        if rectangle % 2 == 0:
            turtle.pencolor(color)
            turtle.forward(l)
            turtle.left(90)
        else:
            turtle.pencolor(color)
            turtle.forward(w)
            turtle.left(90)

def house(color, side):
    for triangle in range(3):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(120)

    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.right(90)

def square(color, side):
    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.right(90)

new_image(-160, 0)
house('blue', 90)
new_image(100, 0)
house('blue', 90)
new_image(-70, -75)
rectangle('red', 90)
new_image(-132, -20)
square('blue', 35)
new_image(130, -20)
square('blue', 35)

=======
import turtle

turtle.speed(0)
turtle.width(3)


def new_image(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(color, side):
    l = 170
    w = 50
    for rectangle in range(4):
        if rectangle % 2 == 0:
            turtle.pencolor(color)
            turtle.forward(l)
            turtle.left(90)
        else:
            turtle.pencolor(color)
            turtle.forward(w)
            turtle.left(90)

def house(color, side):
    for triangle in range(3):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(120)

    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.right(90)

def square(color, side):
    for square in range(4):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.right(90)

new_image(-160, 0)
house('blue', 90)
new_image(100, 0)
house('blue', 90)
new_image(-70, -75)
rectangle('red', 90)
new_image(-132, -20)
square('blue', 35)
new_image(130, -20)
square('blue', 35)

>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
turtle.Screen().exitonclick()