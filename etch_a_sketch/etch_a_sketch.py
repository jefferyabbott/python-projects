from turtle import Turtle, Screen

t = Turtle()


screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_left():
    t.left(5)

def move_right():
    t.right(5)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="space", fun=clear)
screen.exitonclick()