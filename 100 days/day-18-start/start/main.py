from random import *
# from turtle import Turtle, Screen
import turtle as T

tim = T.Turtle()
screen = T.Screen()
T.colormode(255)


"""making doted line."""
# for i in range(10):
#     turtle.forward(10)
#     turtle.up()
#     turtle.forward(10)
#     turtle.down()

"""this program draw shape as any angle you want"""
colors = ['blue', 'red', 'green', 'orange', 'tomato', 'dodger blue']
#
# def draw_shape(number_of_sides):
#     for i in range(number_of_sides):
#         tim.forward(100)
#         tim.right(360 / number_of_sides)
#
# for angele in range(3,10):
#     draw_shape(angele)
#     tim.color(choice(colors))


"""unlimited random colors"""
def rand_color():
    hexa =[0,1,2,3,4,5,6,7,8,9,'a','b','c','d']
    hex = "#"
    for i in range(6):
        hex+= str(choice(hexa))
    return hex

def rand_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b



"""Random walk"""
tim.pensize(30)
tim.speed(0)
# directions = [0, 90, 180, 270]
# for i in range(200):
#     tim.setheading(choice(directions))
#     tim.forward(30)
#     tim.color(rand_rgb())


tim.speed(0)
"""Draw many circles"""
def draw_circles(n):
    t = 360 // n
    for i in range(n):
        tim.circle(100)
        tim.left(t)
        tim.color(rand_rgb())

draw_circles(3)



screen.exitonclick()
