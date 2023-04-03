import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

yaxis = 0
for index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=yaxis)
    yaxis -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You Won!')
            else:
                print('You lost!')

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
print(all_turtles)