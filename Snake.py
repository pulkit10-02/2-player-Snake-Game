from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTIONS = ()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self, player_position, player_color):
        super().__init__()
        self.segments = []
        self.hideturtle()
        self.position = player_position
        self.color = player_color
        self.create_snake()
        self.set_head()

    def create_snake(self, ):
        for pos in self.position:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(self.color)
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def set_head(self):
        self.head = self.segments[0]
        self.head.setheading(UP)
        self.head.color("white")

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_game(self):
        for snakes in self.segments:
            snakes.goto(1100, 1100)
        self.segments.clear()
        self.create_snake()
        self.set_head()
