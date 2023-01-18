import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
# timmy_the_turtle.color("red")

# TODO: Creating a square

dist = 100

n_sides = 3
max_sides = 10
get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))
colors_list = get_colors(max_sides) # sample return:  ['#8af5da', '#fbc08c', '#b741d0', '#e599f1', '#bbcb59', '#a2a6c0']
while n_sides <= max_sides:
    ang = 360/n_sides
    for i in range(n_sides):
        tim.right(ang)
        tim.forward(dist)
    n_sides += 1
    tim.color(colors_list[n_sides-3])



# TODO: turtle moves through a dashed line
# 10 steps followed by 10 spaces and so on - repeated 10 times
# turtle.pencolor("red")
# turtle.forward(100)

# for i in range(10):
#     timmy_the_turtle.pencolor("red")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pencolor("white")
#     timmy_the_turtle.forward(10)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#

screen = Screen()
screen.exitonclick()