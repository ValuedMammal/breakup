from turtle import Turtle

# try:
#     score = int(open('highScore.txt', 'r').read())
# except FileNotFoundError:
#     score = open('highScore.txt', 'w').write(str(0))
# except ValueError:
#     score = 0

FONT = ('Monaco', 13, 'normal')


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color('light cyan')
        self.up
        self.hideturtle()
        # self.highScore = score
        self.goto(-360, 275)
        self.lives = lives
        self.ball_speed = 2
        self.score = 0
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        if self.ball_speed > 10:
            self.write(f"lives: {self.lives} | speed: {self.ball_speed} |  INSANE!", align='left', font=FONT)
        elif self.ball_speed >= 7:
            self.write(f"lives: {self.lives} | speed: {self.ball_speed} |  ON FIRE!", align='left', font=FONT)
        elif self.ball_speed >= 5:
            self.write(f"lives: {self.lives} | speed: {self.ball_speed} |  LIT!", align='left', font=FONT)
        else:
            self.write(f"lives: {self.lives} | speed: {self.ball_speed}", align='left', font=FONT)

    def incr_speed(self):
        self.ball_speed += 1
        self.update_score()
    
    def decr_speed(self):
        self.ball_speed -= 0.5
        self.update_score()

    # def incr_score(self):
    #     self.score += 1
    #     if self.score > self.highScore:
    #         self.highScore += 1
    #     self.update_score()

    def decr_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        # open('highScore.txt', 'w').write(str(self.highScore))
