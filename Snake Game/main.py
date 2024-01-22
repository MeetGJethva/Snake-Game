from turtle import Screen
import time

from snake_body import SnakeBody
from snake_movement import Movement
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.title("My Game")
screen.tracer(0)

body = SnakeBody()
score = ScoreBoard()
movement = Movement()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    movement.move_forward(body)

    if body.get_snakes()[0].distance(food) < 15:
        food.refresh()
        score.update_score()
        body.increse_size()

    if body.get_snakes()[0].xcor() > 290 or body.get_snakes()[0].ycor() > 290 or body.get_snakes()[0].xcor() < -290 or body.get_snakes()[0].ycor() < -290:
        game_is_on = False
        score.game_over()

    # collision with snake
    for i in body.snake_list[1:]:
        if body.snake_list[0].distance(i) < 9:
            game_is_on = False
            print("game_is_on")
            score.game_over()  

    screen.listen()
    screen.onkey(key="Right", fun=movement.right)
    screen.onkey(key="Left", fun=movement.left)
    screen.onkey(key="Up", fun=movement.up)
    screen.onkey(key="Down", fun=movement.down)


screen.exitonclick()