from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color: ")
colors = ["red", "yellow", "green", "blue", "purple"]

def turtle_initialize(turtle_color, x_value = -230, y_value = -100, inc = 0):
    # Initializing the turtle
    tim_turtle = Turtle(shape="turtle")
    tim_turtle.color(turtle_color)

    # Lifting the pen so that it does not draw line
    tim_turtle.penup()

    # Goto starting line
    tim_turtle.goto(x=x_value, y=y_value+inc)


# Initializing 5 turtles
for i in range(5):
    turtle_initialize(turtle_color=colors[i], inc=40*i)


screen.exitonclick()