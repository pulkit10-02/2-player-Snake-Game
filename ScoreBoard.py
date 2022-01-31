from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, name, pos, color):
        super().__init__()
        self.hideturtle()
        self.name = name
        self.score = 0
        self.position = pos
        self.color(color)
        self.penup()
        self.goto(pos)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.name}: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
