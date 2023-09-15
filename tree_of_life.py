<<<<<<< HEAD
#Recursice Fractal Turtle Art
#Keith Jackson from Tonumoy Mukherjee

=======
#Keith Jackson from Tonumoy Mukherjee


>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
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
<<<<<<< HEAD
colormode(255)

def draw(l):  # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:
        turtle.pensize(10)  # Setting Pensize
=======
turtle.width(5)
colormode(255)


def draw(l): #recursive function taking length 'l' as argument
    if(l<10):
        return
    else:

        turtle.pensize(2) #Setting Pensize
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
<<<<<<< HEAD
        turtle.forward(l)  # moving turtle forward by 'l'
        turtle.left(30)  # moving the turtle 30 degrees towards left
        draw(6 * l / 7)  # drawing a fractal on the left of the turtle object 'turtle' with 3/4th of its length
        turtle.right(60)  # moving the turtle 60 degrees towards right
        draw(6 * l / 7)  # drawing a fractal on the right of the turtle object 'turtle' with 3/4th of its length
        turtle.left(30)  # moving the turtle 30 degrees towards left
        turtle.backward(l)  # returning the turtle back to its original position

draw(30)  # drawing 30 times
turtle.right(90)
turtle._tracer(False)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(10)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(6 * l / 7)
        turtle.right(60)
        draw(6 * l / 7)
        turtle.left(30)
        turtle.backward(l)

draw(30)
turtle.left(270)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(10)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(6 * l / 7)
        turtle.right(60)
        draw(6 * l / 7)
        turtle.left(30)
        turtle.backward(l)

draw(30)
turtle.right(90)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(10)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(6 * l / 7)
        turtle.right(60)
        draw(6 * l / 7)
        turtle.left(30)
        turtle.backward(l)

draw(30)
turtle.right(90)
turtle._update()
turtle._tracer(True)

def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(6)
        turtle.pencolor('green')
        turtle.forward(l)
        turtle.left(30)
        draw(5 * l / 6)
        turtle.right(60)
        draw(5 * l / 6)
        turtle.left(30)
        turtle.backward(l)

draw(50)
turtle.right(90)
turtle._update()
turtle._tracer(False)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(6)
        turtle.pencolor('red')
        turtle.forward(l)
        turtle.left(30)
        draw(5 * l / 6)
        turtle.right(60)
        draw(5 * l / 6)
        turtle.left(30)
        turtle.backward(l)

draw(50)
turtle.left(270)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(6)
        turtle.pencolor('magenta')
        turtle.forward(l)
        turtle.left(30)
        draw(5 * l / 6)
        turtle.right(60)
        draw(5 * l / 6)
        turtle.left(30)
        turtle.backward(l)

draw(50)
turtle.right(90)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(6)
        turtle.pencolor('orange')
        turtle.forward(l)
        turtle.left(30)
        draw(5 * l / 6)
        turtle.right(60)
        draw(5 * l / 6)
        turtle.left(30)
        turtle.backward(l)

draw(50)
turtle.right(90)
turtle._update()
turtle._tracer(True)

def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(4 * l / 5)
        turtle.right(60)
        draw(4 * l / 5)
        turtle.left(30)
        turtle.backward(l)

draw(70)
turtle.right(90)
turtle._update()
turtle._tracer(False)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(4 * l / 5)
        turtle.right(60)
        draw(4 * l / 5)
        turtle.left(30)
        turtle.backward(l)

draw(70)
turtle.left(270)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(4 * l / 5)
        turtle.right(60)
        draw(4 * l / 5)
        turtle.left(30)
        turtle.backward(l)

draw(70)
turtle.right(90)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
=======
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
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.forward(l)
        turtle.left(30)
<<<<<<< HEAD
        draw(4 * l / 5)
        turtle.right(60)
        draw(4 * l / 5)
        turtle.left(30)
        turtle.backward(l)

draw(70)
turtle._update()
turtle._tracer(True)
turtle.right(180)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        ran_col = ['saddle brown', 'yellow', 'orange', 'magenta', 'green']
        col_choice = random.choice(ran_col)
        turtle.pencolor(col_choice)
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(120)
turtle.right(90)
turtle._update()
turtle._tracer(False)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        ran_col = ['saddle brown', 'yellow', 'orange', 'magenta', 'green']
        col_choice = random.choice(ran_col)
        turtle.pencolor(col_choice)
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(120)
turtle.right(90)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        ran_col = ['saddle brown', 'yellow', 'orange', 'magenta', 'green']
        col_choice = random.choice(ran_col)
        turtle.pencolor(col_choice)
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(120)
turtle.right(90)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(2)
        ran_col = ['saddle brown', 'yellow', 'orange', 'magenta', 'green']
        col_choice = random.choice(ran_col)
        turtle.pencolor(col_choice)
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(120)

turtle._update()
turtle._tracer(True)
#draw(140)
turtle.right(80)

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
        turtle.backward(l)

draw(140)
turtle._update()
turtle._tracer(False)
turtle.right(30)

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
        turtle.backward(l)

draw(140)
turtle.right(140)

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
        turtle.backward(l)

draw(140)
turtle.right(30)

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
        turtle.backward(l)

draw(140)
turtle.right(140)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
        turtle.pencolor('orange')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(160)
turtle.right(60)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
        turtle.pencolor('orange')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(160)
turtle.right(120)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
        turtle.pencolor('orange')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(160)
turtle.right(60)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(4)
        turtle.pencolor('orange')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(160)
turtle.right(150)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(8)
        turtle.pencolor('red')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(200)
turtle.right(180)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle.pensize(8)
        turtle.pencolor('red')
        turtle.forward(l)
        turtle.left(30)
        draw(3 * l / 4)
        turtle.right(60)
        draw(3 * l / 4)
        turtle.left(30)
        turtle.backward(l)

draw(200)
=======
        draw(6*l/7)
        turtle.right(60)
        draw(6*l/7)
        turtle.left(30)
        turtle.pensize(2)
        turtle.backward(l)
draw(60)
>>>>>>> bafb1563ed5a02d145cf1360dc67919f6b31dd9e
turtle._update()

wn.exitonclick()
