from turtle import Turtle,Screen
from paddle import Paddle
import time
from  ball import Ball
from scoreboard import Scores

screen=Screen()
screen.setup(width=800,height=600)
screen.title("Ghana TT")
screen.bgcolor("black")

screen.listen()
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.onkey(right_paddle.UP, "Up")
screen.onkey(right_paddle.DOWN, "Down")
screen.onkey(left_paddle.UP, "w")
screen.onkey(left_paddle.DOWN, "s")

ball= Ball()

scores = Scores()
Game_ON= True

while Game_ON:

    screen.update()
    time.sleep(ball.speedster)
    ball.move()
    # bounce_y will wall is needed
    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce_y()
    #collision with right paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or (ball.distance(left_paddle)<60 and ball.xcor()<-320):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.resetposition()
        scores.increase_left()


    if ball.xcor() < -380:
        ball.resetposition()
        scores.increase_right()

    if ((scores.left_score+scores.right_score)>3 and abs((scores.left_score-scores.right_score))>0) :
        scores.gameOver()
        print(scores.left_score + scores.right_score)
        Game_ON=False










screen.exitonclick()