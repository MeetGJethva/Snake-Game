from turtle import Turtle

class Movement():
    snake_list = []
    def move_forward(self, body):
        self.snake_list = body.get_snakes()
        for snake in range(len(self.snake_list) -1, 0, -1):
            new_x = self.snake_list[snake -1].xcor()
            new_y = self.snake_list[snake -1].ycor()
            self.snake_list[snake].goto(x= new_x, y= new_y)
        self.snake_list[0].forward(10)
            

    def right(self):
        if self.snake_list[0].heading()!= 180:
            self.snake_list[0].setheading(0)
    
    
    def left(self):
        if self.snake_list[0].heading()!= 0:
            self.snake_list[0].setheading(180)


    def up(self):
        if self.snake_list[0].heading()!= 270:
            self.snake_list[0].setheading(90)


    def down(self):
        if self.snake_list[0].heading()!= 90:
            self.snake_list[0].setheading(270)
