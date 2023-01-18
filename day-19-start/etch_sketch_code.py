from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


# # TODO: Defining a function and assigning a function to another function
# def move_forward():
#     tim.forward(10)
#
# screen.onkey(key="space", fun=move_forward)
# screen.listen()
# screen.exitonclick()

# TODO:
#  w: Moving forward
#  s: Move backward
#  a: Counter-clockwise
#  d: Clockwise
#  c: clear drawing


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise(ang=10):
    tim.left(ang)

def clockwise(ang=10):
    tim.right(ang)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    # tim.reset()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()