from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
screen.listen()
food = Food()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.heat.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.heat.xcor() < -280 or snake.heat.xcor() > 280 or snake.heat.ycor() < -280 or snake.heat.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.heat.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
