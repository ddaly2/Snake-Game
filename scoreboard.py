from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
STARTING_SCORE = 0
SCORE_INCREMENT = 1

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = STARTING_SCORE
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)


    def increase_score(self):
        self.clear()
        self.goto(0, 270)
        self.score += SCORE_INCREMENT
        self.update_scoreboard()