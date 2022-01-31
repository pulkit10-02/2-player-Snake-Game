import time
from turtle import Turtle


class Timer1(Turtle):
    def __init__(self, start_time):
        super().__init__()
        self.start = start_time
        self.counter = 0

    def start_counter(self):
        self.clear()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.counter = int(time.time() - self.start)
        self.write(self.counter, align='center', font=('Courier', 24, 'bold'))
