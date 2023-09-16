import turtle

turtle.speed(0)
turtle.width(3)

def new_image(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(color):
    l = 20
    w = 200
    for rectangle in range(4):
        if rectangle % 2 == 0:
            turtle.pencolor(color)
            turtle.forward(l)
            turtle.right(90)
        else:
            turtle.pencolor(color)
            turtle.forward(w)
            turtle.right(90)

def octagon(color, side):
    for octagon in range(8):
        turtle.pencolor(color)
        turtle.forward(side)
        turtle.left(45)

new_image(0, 0)
rectangle('gray')
new_image(-30, 0)
octagon('red', 75)


turtle.Screen().exitonclick()