import turtle as t
import random as r
sc = t.Screen()
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

is_game_on = False
sc.setup(width=500,height=400)
user_bet = sc.textinput(title="Place your bet!",prompt="Which color is going to win?")
x = -230
y = 150
all_turtles = []

for i in range(len(colors)):
    tim = t.Turtle(shape="turtle")
    tim.speed(6)
    tim.color(colors[i])
    all_turtles.append(tim)
    tim.penup()
    tim.goto(x,y)
    y -= 50

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winner = turtle.pencolor()
            if winner.lower() == user_bet.lower():
                print(f"You Won! {winner} is the Winner.")
            else:
                print(f"You Lost! {winner} is the Winner.")
            break
        dist_to_cover = r.random()*10
        turtle.forward(dist_to_cover)


sc.exitonclick()
