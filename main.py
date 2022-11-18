# 

import turtle as tr
from pad import Paddle
from ball import Ball
from bricks import Bricks
from score import Scoreboard
from ui import UI
import time

screen = tr.Screen()
screen.setup(width=800, height=600)
screen.bgcolor(0, 0, 0.15)
screen.title('')
screen.tracer(0)

pad = Paddle()
ball = Ball()
bricks = Bricks()
score = Scoreboard(lives=5)

ui = UI()
ui.header()

screen.listen()
screen.onkey(key='s', fun=pad.left)
screen.onkey(key='d', fun=pad.right)

def check_borders():
    global ball, score
    # left/right
    if ball.xcor() < -390 or ball.xcor() > 380:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    # upper
    if ball.ycor() > 290:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # lower
    if ball.ycor() < -295:
        score.ball_speed = 2
        score.decr_lives()
        ball.reset()
        if score.lives == 0:
            ball.dx = 0
            ball.dy = 0
            ui.game_over(win=False)
            return
        return

def pad_wrap():
    if pad.xcor() < -420:
        pad.goto(420, -280)
        return
    if pad.xcor() > 420:
        pad.goto(-420, -280)
        return
        
def check_pad():
    global ball, pad, score
    pad_x = pad.xcor()
    ball_x = ball.xcor()

    if ball.distance(pad) < 40 and ball.ycor() < -270:
        # left screen
        if pad_x < -120:
            if ball_x < pad_x - 8:
                ball.sety(-270)
                ball.bounce(x_bounce=True, y_bounce=True)
                if ball.dx < -2:
                    ball.dx += 0.50
                    score.decr_speed()
                elif ball.dx > 2:
                    ball.dx -= 0.5
                    score.decr_speed()
                return
            else:
                ball.sety(-270)
                ball.bounce(x_bounce=False, y_bounce=True)
                if ball.dx < 0:
                    ball.dx -= 1
                else:
                    ball.dx += 1
                score.incr_speed()
                return
        # right screen
        if pad_x > 120:
            if ball_x > pad_x + 8:
                ball.sety(-270)
                ball.bounce(x_bounce=True, y_bounce=True)
                if ball.dx > 2:
                    ball.dx -= 0.5
                    score.decr_speed()
                elif ball.dx < -2:
                    ball.dx += 0.5
                    score.decr_speed()
                return
            else:
                ball.sety(-270)
                ball.bounce(x_bounce=False, y_bounce=True)
                if ball.dx > 0:
                    ball.dx += 1
                else:
                    ball.dx -= 1
                score.incr_speed()
                return
        # middle
        else:
            ball.sety(-270)
            ball.bounce(x_bounce=False, y_bounce=True)
            if ball.dx > 0:
                ball.dx += 1
            else:
                ball.dx -= 1
            score.incr_speed()
            return

def check_brick():
    global ball, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 30:
            # score.incr_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(2000, 2000)
                bricks.bricks.remove(brick)
            
            # left/right bounce
            if ball.xcor() < brick.left_edge or ball.xcor() > brick.right_edge:
                ball.bounce(x_bounce=True, y_bounce=False)

            # up/down bounce
            if ball.ycor() < brick.low_edge or ball.ycor() > brick.up_edge:
                ball.bounce(x_bounce=False, y_bounce=True)

while True:
    screen.update()
    # time.sleep(0.005)
    ball.move()

    if len(bricks.bricks) == 0:
        ball.dx = 0
        ball.dy = 0
        ui.game_over(win=True)
    
    pad_wrap()

    check_borders()

    check_pad()

    check_brick()

tr.mainloop()