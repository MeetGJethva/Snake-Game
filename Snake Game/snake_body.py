from turtle import Turtle

class SnakeBody():
    snake_list = []

    def __init__(self):
        self.x = 0
        for _ in range(3):
            new_snake = Turtle('square')
            new_snake.penup()
            new_snake.goto(x= self.x, y= 0)
            self.x-=20
            self.snake_list.append(new_snake)

    def increse_size(self):
        new_snake = Turtle('square')
        new_snake.penup()
        new_snake.goto(x= self.snake_list[-1].xcor(), y= self.snake_list[-1].ycor())
        self.snake_list.append(new_snake)

    
    def get_snakes(self):
        return self.snake_list
