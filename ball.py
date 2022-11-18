from turtle import Turtle
import random

POS_DELTA = 2
DIRECTION = [-1, 1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.dx = POS_DELTA
        self.dy = -2
        self.reset()

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.dx *= -1
        if y_bounce:
            self.dy *= -1

    def reset(self):
        self.goto(0, -30)
        self.dx = random.choice(DIRECTION) * POS_DELTA
        self.dy = random.choice(DIRECTION) * POS_DELTA
            

    