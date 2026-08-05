import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300,random.randint(-230,230))
            self.all_cars.append(new_car)
            print(len(self.all_cars))

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() > -300:
                car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT