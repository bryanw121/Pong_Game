from turtle import Turtle


class Scoreboard(Turtle):
    """updates the score for both the user and the computer"""
    def __init__(self, x_pos, y_pos, score):
        super().__init__()
        self.score = score
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.update()

    def update(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setx(self.x_pos)
        self.sety(self.y_pos)
        self.write(f"{self.score}", False, 'center', ('Arial', 70, 'normal'))

    def increase_score(self):
        self.score += 1

