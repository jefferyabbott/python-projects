from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

t = Turtle()
t.hideturtle()
t.speed("fastest")
colormode(255)

def draw_spirograph(circle_size, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.setheading(t.heading() + size_of_gap)
        t.color(random_color())
        t.circle(circle_size)


size = 'X'
gap = 'X'

while not size.isdigit() and not gap.isdigit():
    size = input("Set the size of the spirograph (must be greater than 0) ]")
    gap = input("Set the gap size of the spirograph angles (must be greater than 0) ]")

size = int(size)
gap = int(gap)

draw_spirograph(size, gap)

screen = Screen()
screen.exitonclick()
