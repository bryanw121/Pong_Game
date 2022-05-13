import turtle
from turtle import Turtle

class Paddle(Turtle):
    """Paddle is used to hit the ball. There should be one paddle on each side of the screen"""
    def __init__(self, starting_x, starting_y):
        super().__init__()
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.create_paddle()

    def create_paddle(self):
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(self.starting_x, self.starting_y)

    def move_up(self):
        y_cord = self.ycor()
        y_cord += 20
        self.sety(y_cord)

    def move_down(self):
        y_cord = self.ycor()
        y_cord -= 20
        self.sety(y_cord)

    def paddle_pos(self):
        return self.pos()