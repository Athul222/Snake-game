from Snake_file import Snake
from turtle import Turtle, Screen
from Snake_Food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.Up, key="Up")
screen.onkey(fun=snake.Down, key="Down")
screen.onkey(fun=snake.Left, key="Left")
screen.onkey(fun=snake.Right, key="Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    #Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        
    #Detect the collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    #if the head collides with the any of the segments :
            #trigger  game_over
screen.exitonclick()