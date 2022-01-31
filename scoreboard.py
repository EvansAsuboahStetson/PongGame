from turtle import Turtle
class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score=0
        self.left_score=0
        self.penup()
        self.hideturtle()
        self.color("white")

        self.updatescore()


    def updatescore(self):
        self.goto(-100, 200)
        self.write( self.left_score , move=False, align='center', font=('Arial', 30, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, move=False, align='center', font=('Arial', 30, 'normal'))
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=('Arial', 30, 'normal'))
        self.goto(0, -50)
        if self.right_score > self.left_score:
            self.write("Nnifa no Afa!",move=False, align='center', font=('Arial', 30, 'normal'))
        elif self.left_score > self.right_score:
            self.write("Benkum adi nkunim!",move=False, align='center', font=('Arial', 30, 'normal'))


    def increase_right(self):
        self.right_score += 1
        self.clear()
        self.updatescore()

    def increase_left(self):
        self.left_score += 1
        self.clear()
        self.updatescore()
