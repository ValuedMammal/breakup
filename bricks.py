from turtle import Turtle
import random

COLORS = ['SteelBlue', 'RoyalBlue', 'LightSkyBlue', 'DarkTurquoise', 
'Turquoise', 'Cyan', 'DarkCyan', 'Aquamarine',
'PaleVioletRed', 'Magenta', 'Orchid', 'Plum', 
'Pink', 'MediumVioletRed', 'HotPink', 'LightCoral']


WEIGHT = 1
# array of random block weights 1, 2, 3, etc
# weights = []
# random.randint(1, 2)

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.up()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.goto(x_cor, y_cor)

        self.quantity = WEIGHT

        self.left_edge = self.xcor() - 30
        self.right_edge = self.xcor() + 30
        self.up_edge = self.ycor() + 10
        self.low_edge = self.ycor() - 10

class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 220
        self.bricks = []
        self.create_all()

    def create_lane(self, y_cor):
        for i in range (-320, 360, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all(self):
        for i in range(self.y_start, self.y_end, 22):
            self.create_lane(i)


