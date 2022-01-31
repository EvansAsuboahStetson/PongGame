from turtle import Turtle

WIDTH = 20
HEIGHT = 100
X_POS = 350
Y_POS = 0


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.create_paddle()


    def create_paddle(self):
        self.shape("square")
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.position)

    def UP(self):
        x_postion = self.xcor()
        y_position = self.ycor()
        self.goto(x_postion, y_position + WIDTH)

    def DOWN(self):
        x_postion = self.xcor()
        y_position = self.ycor()
        self.goto(x_postion, y_position - WIDTH)
