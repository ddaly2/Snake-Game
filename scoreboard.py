from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
SCORE_INCREMENT = 1

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.goto(0, 270)
        self.score += SCORE_INCREMENT
        self.update_scoreboard()
