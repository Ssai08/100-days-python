from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 11, 'normal')
SCORE_POSITION = (0,280)

with open("data.txt",mode = "r") as data:
    score = data.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = int(score)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}; High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update_score()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.current_score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER!",align=ALIGNMENT,font=FONT)

