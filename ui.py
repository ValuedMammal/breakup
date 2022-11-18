import time
from turtle import Turtle
import random

FONT = ('Monaco', 24, 'normal')
ALIGN = 'center'
COLOR = 'white'
COLORS = ['SteelBlue', 'RoyalBlue', 'LightSkyBlue', 'DarkTurquoise', 
'Turquoise', 'Cyan', 'DarkCyan', 'Aquamarine', 
'PaleVioletRed', 'Magenta', 'Orchid', 'Plum', 
'Pink', 'MediumVioletRed', 'HotPink', 'LightCoral']

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color(random.choice(COLORS))
        self.header()

    def header(self):
        self.clear()
        self.goto(0, -135)
        self.write('the breakup', align=ALIGN, font=FONT)    

    def game_over(self, win):
        self.clear()
        if win == True:
            self.write('heartbreaker!', align=ALIGN, font=FONT)
        else:
            self.write('dumped!', align=ALIGN, font=FONT)
