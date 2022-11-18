# "the breakup"

This is a simple brick-breaking game made with python using the turtle module. Turtle is a simple graphics interface that originally dates back to the late 1960's and which Python continues to support today - [python docs](https://docs.python.org/3/library/turtle.html).  

I used the tutorial at [geeksforgeeks.org](https://www.geeksforgeeks.org/create-breakout-game-using-python/) to build the game following much of the structure and mechanics, however I changed a number of parameters and tweaked some of the logic to my liking. This way, I was able to check my learning along the way. The tutorial by [@Ishan2608](https://github.com/Ishan2608) does a good job of building the project step by step.  

I initially encountered an issue where the screen failed to render due to a deprecated 'tkinter' library while using python 3.8.x. Upgrading to python 3.11 fixed the issue, allowing everything to run smoothly on the M1 Mac.  

All the objects - the bricks, ball, and paddle - are turtle objects given the shape of 'square,' or 'circle' in the case of the ball. A turtle object has default dimensions of 20x20 and can be scaled appropriately. For example I used dimensions of 10x10 for the ball, 10x80 for the paddle, and 20x60 for the bricks, given a screen size of 800x600. In python the on-screen objects are implemented as classes which themselves allow for various methods and functionality.  

Some of the fun additions I made are to allow the paddle to wrap to the opposite side when the user scrolls off screen, and I added logic to change the ball's velocity in the x direction upon contact with the paddle. The code in the tutorial implements a scoreboard which can read/write the high score to a txt file, but I have that turned off in the demo. The tutorial also allows the user to pause the game by placing the main loop under a simple boolean. I chose not to include that here, but it would be good practice to solidify the relevant concepts.  

## Screens

![](/doc/break-screen1.png?raw=true)  

![](/doc/break-screen2.png?raw=true)  

![](/doc/break-screen3.png?raw=true)
