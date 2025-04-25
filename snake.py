from turtle import Turtle, Screen
from scoreboard import Scoreboard
screen= Screen()


position =[(0,0), (-20, 0) , (-40, 0)]
tims = []
class Snake():
    def __init__(self):
        for i in position:
            self.tim = Turtle()
            self.tim.penup()
            self.tim.shape("square")
            self.tim.color("white")
            self.tim.setpos(i)
            tims.append(self.tim)
            self.head = tims[0]

    def increase(self):
        self.newtim = Turtle()
        self.newtim.penup()
        self.newtim.shape("square")
        self.newtim.color("white")
        xco = tims[len(tims)-1].xcor()
        yco = tims[len(tims)-1].ycor()
        self.newtim.goto(xco, yco)
        tims.append(self.newtim)


    def move(self):
            for i in range(len(tims) - 1, 0, -1):
                tims[i].goto(tims[(i - 1)].pos())

                def turn_right():
                    tims[0].setheading(0)

                def turn_up():
                    tims[0].setheading(90)

                def turn_left():
                    tims[0].setheading(180)

                def turn_down():
                    tims[0].setheading(270)

                screen.listen()
                screen.onkey(key="Up", fun=turn_up)
                screen.onkey(key="Down", fun=turn_down)
                screen.onkey(key="Right", fun=turn_right)
                screen.onkey(key="Left", fun=turn_left)
                # screen.onkey(key="c", fun=clear)
            tims[0].forward(20)

    def reset(self):
        for i in tims:
            i.goto(1000,1000)
        tims.clear()
        Snake()












