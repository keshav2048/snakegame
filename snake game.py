from turtle import  Screen,Turtle
import time
from snake import Snake, tims
from food import Food

from scoreboard import Scoreboard
scoreboard = Scoreboard()

food = Food()
screen = Screen()
screen.title(" Snake Game ")
screen.bgcolor("black")
screen.setup(500, 500)
screen.tracer(0)

snake=Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    for i in tims[1:len(tims) - 1]:
        if tims[0].distance(i) == 0:
            snake.reset()
            # writer.write("GAME OVER", False, "center")
            scoreboard.reset()

    if tims[0].distance(food) < 15:
        scoreboard.increase_scoreboard()
        food.new_location()
        snake.increase()

    if tims[0].xcor() > 250 or tims[0].xcor() < -250 or tims[0].ycor() > 250 or tims[0].ycor() < -250:
        scoreboard.reset()
        snake.reset()
        # writer.write("GAME OVER", False, "center")



screen.exitonclick()