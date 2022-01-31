import turtle
from turtle import *

from Food import *
from ScoreBoard import *
from Snake import *
from gametimer import *

# CONSTANTS
STARTING_POSITION_1 = [(30, 0), (30, -20), (30, -40)]
PLAYER_1_Color = 'yellow'
SCOREBOARD_1 = (250, 310)

STARTING_POSITION_2 = [(-30, 0), (-30, -20), (-30, -40)]
PLAYER_2_Color = 'cyan'
SCOREBOARD_2 = (-250, 310)

# SETTING UP THE SCREEN
game_screen = Screen()
game_screen.setup(width=1.0, height=1.0)
game_screen.bgcolor("black")
game_screen.title("Snake Game")

# TAKING PLAYER NAMES
player_1 = game_screen.textinput(title='Snake Game', prompt="Enter player 1:").title()
player_2 = game_screen.textinput(title='Snake Game', prompt="Enter player 2:").title()

game_screen.tracer(0)

# CREATING 2 SNAKES
snake1 = Snake(STARTING_POSITION_1, PLAYER_1_Color)
snake2 = Snake(STARTING_POSITION_2, PLAYER_2_Color)

# GROWING THE FOOD
food = Food()

# PLAYER SCOREBOARDS
scoreboard_player1 = Scoreboard(player_1, SCOREBOARD_1, PLAYER_1_Color)
scoreboard_player2 = Scoreboard(player_2, SCOREBOARD_2, PLAYER_2_Color)

# ASSIGNING CONTROLS
game_screen.listen()
game_screen.onkey(snake1.up, "Up")
game_screen.onkey(snake1.down, "Down")
game_screen.onkey(snake1.left, "Left")
game_screen.onkey(snake1.right, "Right")

game_screen.onkey(snake2.up, "w")
game_screen.onkey(snake2.down, "s")
game_screen.onkey(snake2.left, "a")
game_screen.onkey(snake2.right, "d")


def declare_winner(winner_name, winner_color):
    turtle.hideturtle()
    turtle.color(winner_color)
    turtle.pendown()
    turtle.home()
    turtle.write(f"{winner_name} wins!!", align='center', font=('Courier', 40, 'bold'))
    time.sleep(3)
    turtle.clear()
    # counter.start = time.time()
    scoreboard_player1.reset_game()
    scoreboard_player2.reset_game()
    snake1.reset_game()
    snake2.reset_game()


# counter = Timer1(time.time())

game_is_on = True

while game_is_on:
    # counter.start_counter()
    game_screen.update()
    time.sleep(0.05)
    snake1.move()
    snake2.move()

    # Detect collision with food.
    if snake1.head.distance(food) < 15:
        food.refresh()
        snake1.extend()
        scoreboard_player1.increase_score()
    elif snake2.head.distance(food) < 15:
        food.refresh()
        snake2.extend()
        scoreboard_player2.increase_score()

    # Detect collision with wall.
    if snake1.head.xcor() > 675 or snake1.head.xcor() < -680 or snake1.head.ycor() > 375 or snake1.head.ycor() < -375:
        declare_winner(scoreboard_player2.name, PLAYER_2_Color)
    #
    elif snake2.head.xcor() > 675 or snake2.head.xcor() < -680 or snake2.head.ycor() > 375 or snake2.head.ycor() < -375:
        declare_winner(scoreboard_player1.name, PLAYER_1_Color)

    # Detect collision with tail.
    for segment in snake1.segments:
        if segment == snake1.head:
            pass
        elif snake1.head.distance(segment) < 10:
            declare_winner(scoreboard_player2.name, PLAYER_2_Color)

    for segment in snake2.segments:
        if segment == snake2.head:
            pass
        elif snake2.head.distance(segment) < 10:
            declare_winner(scoreboard_player1.name, PLAYER_1_Color)

    # # Timer runs out. Commented out to make game more fun
    # if counter.counter >= 10:
    #     if scoreboard_player1.score > scoreboard_player2.score:
    #         declare_winner(scoreboard_player1.name, PLAYER_1_Color)
    #     else:
    #         declare_winner(scoreboard_player2.name, PLAYER_2_Color)

    # # DETECT COLLISION WITH EACH OTHER. Commented out to prevent cheating.
    # for snake2_segment in snake2.segments:
    #     for snake1_segment in snake1.segments:
    #         if snake1_segment.distance(snake2_segment) < 10:
    #             declare_winner()

game_screen.mainloop()
