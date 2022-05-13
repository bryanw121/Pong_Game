from turtle import Turtle
import time


class Ball(Turtle):
    """Ball that will continuously move throughout the game and bounce when it makes contact with a surface"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0, 0)
        self.speed = 1.5

    def move(self):
        """moves ball at constant speed"""
        self.forward(self.speed)

    def increase_speed(self):
        self.speed += 0.1

    def bounce_horizontal(self):
        """bounces the ball off a surface at a certain angle"""
        initial_angle = self.heading()
        if 0 <= initial_angle <= 180:
            final_angle = abs(initial_angle-180)
            self.setheading(final_angle)
        elif 180 < initial_angle < 360:
            final_angle = 540 - initial_angle
            self.setheading(final_angle)

    def bounce_wall(self):
        initial_angle = self.heading()
        final_angle = 360 - initial_angle
        self.setheading(final_angle)

    def ball_position(self):
        return self.position()

    def reset_ball_position_r(self):
        self.setposition(0, 0)
        self.seth(155)
        self.speed = 1.5
        time.sleep(.5)

    def reset_ball_position_l(self):
        self.setposition(0, 0)
        self.seth(25)
        self.speed = 1.5
        time.sleep(.5)

