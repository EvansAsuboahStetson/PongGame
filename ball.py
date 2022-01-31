

WIDTH=20
HEIGHT=30
X_MOVE=8
Y_MOVE=8
from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.x_position=0.0
        self.y_position=0.0
        self.createball()
        self.xmove=X_MOVE
        self.ymove =Y_MOVE
        self.speedster=0.1
    def createball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()


        self.goto(self.x_position,self.y_position)
    def move(self):
        new_xcor= self.xcor()+self.xmove
        new_ycor= self.ycor()+self.ymove
        self.goto(new_xcor,new_ycor)
    def bounce_y(self):
        self.ymove*=-1

    def bounce_x(self):
        self.xmove *= -1
        self.speedster *= 0.9
        print(self.speedster)
    def resetposition(self):
       self.home()
       self.speedster=0.1
       self.bounce_x()





