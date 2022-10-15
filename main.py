from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")


gameon = True
while gameon:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()
    if ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_positon()
        score.l_point()

    # Detect left paddle misses:
    if ball.xcor() < -380:
        ball.reset_positon()
        score.r_point()






screen.exitonclick()