from turtle import Turtle

class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(0,-280)
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, 'center', font= ("Verdana", 15, "bold"))

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, 'center', font= ("Verdana", 15, "bold"))
        self.score += 1

