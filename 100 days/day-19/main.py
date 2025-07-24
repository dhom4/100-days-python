from turtle import Turtle, Screen

frank = Turtle()
screen = Screen()

""" Make an Etch-s-sketch app"""
# w = forwards
# s = backwards
# a =counter-clockwise
# d = clockwise
# c = clear all

# def move():    frank.forward(20)
# def back():    frank.backward(30)
# def clock_wise():    frank.right(10)
# def c_clock_wise():    frank.left(10)
# def clear():
#     frank.home()
#     frank.clear()
#
# screen.listen()
# screen.onkey(key="w",fun=move)
# screen.onkey(key="s",fun=back)
# screen.onkey(key="d",fun=clock_wise)
# screen.onkey(key="a",fun=c_clock_wise)
# screen.onkey(key="c",fun=clear)
"""end"""

rafayel = Turtle()
ronaldo = Turtle()

rafayel.shape("turtle")
rafayel.color("red")
ronaldo.shape("turtle")
ronaldo.color("orange")

rafayel.forward(100)
ronaldo.backward(100)


screen.exitonclick()