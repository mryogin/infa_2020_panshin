import turtle
from math import pi, cos, sin


turtle.shape('turtle')
turtle.speed('fastest')

def s_word():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def square(side=50):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)


def circle():
#    turtle.penup()
#    turtle.goto(50, 0)
#    turtle.left(90)
#    turtle.pendown()
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)


def more_squares(number, side=50):
    for i in range(1, number+1):
        square(side)
        turtle.penup()
        turtle.goto(-5*i,-5*i)
        turtle.pendown()
        side += 10


def square_spiral(sides=100, direction='Left'):

    # if direction non left or right
    try:

        #string must work with different keyboard layouts
        direction = direction.lower()

        if direction == 'left':
            for i in range(sides):
                turtle.forward(i * 5)
                turtle.left()
        elif direction == 'right':
            for i in range(sides):
                turtle.forward(i * 5)
                turtle.right(90)
    except: return

def circle_spiral():

    for i in range(400):
        t = i / 10 * pi
        dx = t * cos(t)
        dy = t * sin(t)
        turtle.goto(dx, dy)

def polygon(n, side=30):
    for i in range(n):
        turtle.forward(side)
        turtle.left(360 / n)

def polygon_into_polygon(levels=10, side = 20):
    #first polygon sides
    triangle = 3

    for i in range (levels):
        polygon(triangle, side)
        triangle += 1
        side += 10

def flower(leaves=6):
    pass
    for i in range(leaves):
        circle()
        turtle.left(360/leaves)


