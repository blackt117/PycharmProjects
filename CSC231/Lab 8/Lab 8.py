########################
# Name: Tyler Black
# Due Date: 4/28/23
# Algorithm: Created a function to draw a circle with a random color and random width in Turtle Graphics. This function
#            is passed a random radius, random values of x and y coordinates, and a turtle object.
#
# Resources: Prior Knowledge and Lecture Slides
#
#

import turtle
import math
import random

def drawcircle(circle,center,radius):
    '''
    Purpose: Draw a circle in turtle graphics with a certain radius and x and y coordinates
    Param: circle (turtle object), center(list of integers), and radius (integer)
    Return: None
    '''
    color = ['green','blue','black', 'red', 'yellow','orange','purple', 'pink', 'brown']
    colorint = random.randint(0,8)
    circle.pencolor(color[colorint])
    circle.speed(0)
    x = center[0]
    y = center[1]
    circle.penup()
    circle.setposition(x,y-radius)
    randint = random.randint(3,30)
    circle.pensize(randint)
    circle.pendown()
    for i in range(120):
        circle.forward((2.0 * math.pi * radius) / 120)
        circle.left(3)

def main():
    '''
    Purpose: Create turtle screen and title the window. Call drawcircle function 35 times with different arguments each
             time.
    Param: None
    Return: None
    '''
    turtle.setup(1200, 800)
    window = turtle.Screen()
    window.title('Lab 8: Practice with Turtle')
    circle = turtle.Turtle()
    for i in range(35):
        radius = random.randint(25,150)
        x = random.randint(-500,500)
        y = random.randint(-300,300)
        drawcircle(circle,[x,y],radius)
main()

