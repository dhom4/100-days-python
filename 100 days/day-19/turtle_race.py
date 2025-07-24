from turtle import Turtle, Screen
from random import *

colors = ['red','orange','yellow','green','purple','blue']

# tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle you are fan of?: ")

all_turtles = []
y_postions = [-70, -40, -10, 20, 50, 80]

for t in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-220, y=y_postions[t])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            # turtle.write("🌟")
            turtle.write((0, 0), True)
            is_race_on = False

            if user_bet == turtle.pencolor:
                print(f"you won! {turtle.pencolor()}")
            else:
                print(f"you lost, {turtle.pencolor()} won!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()