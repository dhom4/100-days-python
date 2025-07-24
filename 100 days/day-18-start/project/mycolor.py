import random
import turtle as T

color_list = [
     (39, 30, 21), (121, 90, 66), (244, 217, 102), (225, 233, 241), (148, 162, 173),
     (87, 99, 106), (27, 33, 29), (234, 242, 236), (162, 133, 79), (86, 98, 89), (202, 101, 68), (146, 168, 152),
     (243, 230, 232), (36, 46, 49), (240, 175, 151), (77, 65, 44), (226, 5, 20), (110, 46, 30), (181, 152, 157),
     (113, 95, 98), (180, 191, 206), (170, 206, 175), (228, 69, 79), (109, 139, 119), (57, 68, 61), (232, 168, 173),
     (117, 128, 140), (37, 30, 32)
    ]

tom = T.Turtle()
screen = T.Screen()
T.colormode(255)

tom.speed("fastest")
tom.penup()
tom.hideturtle()


def dots(n):
    for j in range(n):
        tom.dot(30, random.choice(color_list))
        tom.forward(50)

def draw(n):
    x = -200
    y = -200
    for i in range(n):
        tom.teleport(x, y)
        dots(n)
        y += 50


draw(4)


screen.exitonclick()