from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_cord = random.randint(-275, 275)
        random_y_cord = random.randint(-275, 275)
        self.goto(random_x_cord, random_y_cord)