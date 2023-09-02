#Keith Jackson
#polygon_spirals_turtle

import turtle
import random
from turtle import *

turtle.shape('turtle')
turtle.speed(0)
turtle.width(5)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

#forward helper function  
def move(len):
  back(-1*len)

def polygon(num, size):
  for s in range(num):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r,g,b)
    turtle.forward(size)
    turtle.left(360/num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)

for n in range(3, 10):
  n = random.randrange(3, 10)
  move(50) #forward 
  polygon(n, 100/n)
  back(50)
  turtle.right(360/7)
  
turtle.penup()
turtle.goto(-30,20)
turtle.pendown()
spiral(50,90)
