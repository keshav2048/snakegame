from turtle import Turtle, Screen
import random
screen = Screen()
screen.tracer(0)
score = 0
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        xc = random.randint(-240, 240)
        yc = random.randint(-240, 240)
        self.goto(xc, yc)

    def new_location(self):
        self.xc = random.randint(-240, 240)
        self.yc = random.randint(-240, 240)
        self.goto(self.xc, self.yc)
