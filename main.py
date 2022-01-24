from turtle import *
import time
from paddle import *
from ball import *

screen = Screen()
screen.setup(height = 800,width =600)
screen.title('Pong-Game')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((281,0))
l_paddle = Paddle((-290,0))

ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# #Detect Collision With Wall
    if ball.ycor() > 378 or ball.ycor()<-378:
        ball.bounce()

    if ball.ycor()

screen.exitonclick()
