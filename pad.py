from turtle import Turtle

MOVE_DIST = 40

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('light cyan')
        self.shape('square')
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.goto(0, -280)

    def left(self):
        self.backward(MOVE_DIST)
    def right(self):
        self.forward(MOVE_DIST)
