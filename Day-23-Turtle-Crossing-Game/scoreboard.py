from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250.,270)
        self.current_level = 1
        self.show_level()

    def show_level(self):
        self.write(arg=f"Level:{self.current_level}",move=False,align="center",font=("Arial",13,"normal"))

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!",move=False,align="center",font=FONT)


