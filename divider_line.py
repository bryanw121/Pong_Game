from turtle import Turtle

class Divider:
    """Makes a dotted dividing line down the middle of the screen"""
    def __init__(self):
        self.divider_turtle = Turtle()
        self.create_divider()

    def create_divider(self):
        self.divider_turtle.penup()
        self.divider_turtle.color('white')
        self.divider_turtle.width(5)
        self.divider_turtle.hideturtle()
        self.divider_turtle.goto(0, -280)
        self.divider_turtle.setheading(90)
        for i in range(16):
            self.divider_turtle.pendown()
            self.divider_turtle.forward(25)
            self.divider_turtle.penup()
            self.divider_turtle.forward(25)
