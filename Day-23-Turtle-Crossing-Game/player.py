from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#Create a turtle player that starts at the bottom of the screen and
# listen for the "Up" keypress to move the turtle north.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() < 300:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)

    def reset_location(self):
        self.goto(STARTING_POSITION)

