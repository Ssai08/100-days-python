from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time as t
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=1000,height=600)
sc.title("PONG")
sc.bgcolor("black")
sc.tracer(0)

r_paddle = Paddle((450,0))
l_paddle = Paddle((-450,0))
# sc.tracer(1)
ball = Ball()
score = Scoreboard()

sc.listen()
sc.onkeypress(fun=r_paddle.move_up,key="Up")
sc.onkeypress(fun=r_paddle.move_down,key="Down")

sc.onkeypress(fun=l_paddle.move_up,key="w")
sc.onkeypress(fun=l_paddle.move_down,key="s")

sleep_timer = 0.1
game_is_on = True
while game_is_on:
    t.sleep(sleep_timer)
    l_score = score.l_score
    r_score = score.r_score
    sc.update()
    ball.move()

    #Detech collision with the walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detech collision with paddles
    if (440 < ball.xcor() < 470 and ball.distance(r_paddle) < 40) or (-470 < ball.xcor() < -440 and ball.distance(l_paddle) < 40):
        ball.bounce_x()
        print(f"Ball X-coordinate (RIGHT): {ball.xcor()}")
        print(f"Ball distance from right paddle: {ball.distance(r_paddle)}")

    #Detech when ball goes out of bound and the game is over
    if ball.xcor()>480 or ball.xcor()<-480:
        ball.out_of_bound()
        game_is_on = False

    #Store and show the score in the game
    if 440 < ball.xcor() < 470 and ball.distance(r_paddle)<50:
        score.r_point()
        # print(f"Ball X-coordinate (RIGHT): {ball.xcor()}")
        # print(f"Ball distance from right paddle: {ball.distance(r_paddle)}")
    if -470 < ball.xcor() < -440 and ball.distance(l_paddle)<50:
        score.l_point()
        # print(f"Ball X-coordinate (LEFT): {ball.xcor()}")
        # print(f"Ball distance from left paddle: {ball.distance(l_paddle)}")

    #Increase the speed of the ball if any of the side scores a point
    # if (l_score < score.l_score or r_score < score.r_score) and sleep_timer>0.03:
    #     print(f"before: {sleep_timer}")
    #     sleep_timer = round((sleep_timer - 0.01),3)
    #     print(f"After: {sleep_timer}")

sc.exitonclick()