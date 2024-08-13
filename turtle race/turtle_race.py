from turtle import Turtle, Screen, TK
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Place your bet", prompt="Which color turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

start_y = 120
for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(-230, start_y)
    turtles.append(t)
    start_y -= 50

race_in_progress = True
winner_found = False
while race_in_progress:
    for t in turtles:
        t.forward(randint(1,10))
        if t.xcor() >= 240:
            winner_found = True # this should prevent having multiple winners
            if winner_found:
                winner = t.pencolor()
                if winner == user_bet:
                    TK.messagebox.showinfo(title="Congrats! 🎉", message=f"{winner} won the race!")
                else:
                    TK.messagebox.showinfo(title="Sorry ☹️", message=f"{winner} won the race.")
            race_in_progress = False


screen.exitonclick()
