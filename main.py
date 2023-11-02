#Import modules: turtle module is the main one as this will mimic our snake:

from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

all_turtles = []
screen = Screen()

#This will let the screen listen to you:
screen.listen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame!!")
screen.tracer(0)

#Calling the snake,food and score board class:

snake = Snake()
food = Food()
score_board = Score()
game_is_on = True

#This will make the snake move according to your commands:

screen.onkeypress(key="a", fun=snake.turn_left)
screen.onkeypress(key="d", fun=snake.turn_right)
screen.onkeypress(key="s", fun=snake.turn_down)
screen.onkeypress(key="w", fun=snake.turn_up)



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.score()
        snake.extend()
    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        score_board.update_score()
        snake.reset()
    # Detect collision with any segment:
    for segment in snake.all_turtles[-1: 0: -1]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            score_board.update_score()
            snake.reset()



screen.exitonclick()





