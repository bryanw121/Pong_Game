#classes to add: player pad, computer pad, score, dividing line, ball
from turtle import Screen
from paddle import Paddle
from divider_line import Divider
from scoreboard import Scoreboard
from ball import Ball
import time


#constants
right_score = 0
left_score = 0
screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(width=800, height=600)
game_is_live = True
screen.tracer(0) #this turns off animations. Also requires a screen.update() function to actually visualize the program
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
divider = Divider()
r_scoreboard = Scoreboard(100, 200, right_score)
l_scoreboard = Scoreboard(-100, 200, left_score)
ball = Ball()
ball.seth(25)

while game_is_live:
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.move_up, 'Up')
    screen.onkey(r_paddle.move_down, 'Down')
    screen.onkey(l_paddle.move_up, 'w')
    screen.onkey(l_paddle.move_down, 's')
    ball.move()
    if ball.ycor() <= -290 or ball.ycor() >= 290:
        ball.bounce_wall()
    elif r_paddle.distance(ball) <= 15 or l_paddle.distance(ball) <= 15:
        ball.bounce_horizontal()
        ball.increase_speed()
    elif ball.xcor() >= 330 and r_paddle.distance(ball) <= 50:
        ball.bounce_horizontal()
        ball.increase_speed()
    elif ball.xcor() <= -330 and l_paddle.distance(ball) <= 50:
        ball.bounce_horizontal()
        ball.increase_speed()
    elif ball.xcor() >= 400:
        l_scoreboard.increase_score()
        l_scoreboard.update()
        ball.reset_ball_position_r()
    elif ball.xcor() < -420:
        r_scoreboard.increase_score()
        r_scoreboard.update()
        ball.reset_ball_position_l()










screen.exitonclick()