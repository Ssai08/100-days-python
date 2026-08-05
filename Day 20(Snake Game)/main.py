from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

'''
Day 24 Edits:
1. remove game_over method from scoreboard and add reset method both the scoreboard.py and snake.py
2. Add a high score variable to keep track of highscore and update when the current score exceeds previous high score
'''

sc = Screen()
sc.title("Snake Game")
sc.bgcolor("black")
sc.setup(height=600, width=600)
sc.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:

    sc.update()
    time.sleep(0.09)
    snake.move()

    #Detect collision of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        # is_game_on = False
        score.reset()
        snake.reset()
        # score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            # is_game_on = False
            # score.game_over()



sc.exitonclick()