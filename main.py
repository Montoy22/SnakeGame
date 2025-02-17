from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
# head= Turtle(shape="square")
# body =Turtle(shape="square")
# tail =Turtle(shape="square")
# head.color("DodgerBlue")
# body.color("DodgerBlue")
# tail.color("DodgerBlue")
# body.setposition(-20,0)
# tail.setposition(-40,0)
screen.tracer(0)
snake= Snake()
food = Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        #game_is_on=False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        
    #detect collision with tail
    for segments in snake.segments[1:]:
        # if segments==snake.head:
        #     pass
        if snake.head.distance(segments)<10:
            #game_is_on = False
            scoreboard.game_over()


screen.exitonclick()