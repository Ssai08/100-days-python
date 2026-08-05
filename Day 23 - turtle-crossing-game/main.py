import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(fun=player.move,key="Up")
car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    car_manager.move_cars()

    #Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    #Detect when the player has reached the other side
    if player.ycor() > 280:
        player.reset_location()
        score.level_up()
        car_manager.speed_increase()

screen.exitonclick()