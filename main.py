import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from brickwall import BrickWall
from scoreboard import ScoreBoard

WIDTH = 1000
HEIGHT = 800
SCREEN_COLOR = "black"
SCREEN_TITLE = "BREAK OUT GAME"

COLLISION_MARGIN_PADDLE = 100
PADDLE_HEIGHT = 20
COLLISION_MARGIN_BRICK = 20
SCREEN_REFRESH = 0.02

game_score = ScoreBoard()

play_again = True
while play_again:

    screen = Screen()
    screen.bgcolor(SCREEN_COLOR)
    screen.title(SCREEN_TITLE)
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)

    game_wall = BrickWall(game_score.level)
    game_paddle = Paddle()
    game_ball = Ball()
    game_score.refresh()

    screen.listen()
    screen.onkey(game_paddle.move_ship_left, "Left")
    screen.onkey(game_paddle.move_ship_right, "Right")

    game_on = True
    while game_on:
        time.sleep(SCREEN_REFRESH)
        game_ball.move()
        screen.update()

        # check for collisions with paddle
        if game_paddle.ycor() - PADDLE_HEIGHT <= game_ball.ycor() <= game_paddle.ycor() + PADDLE_HEIGHT and \
                game_paddle.distance(game_ball) <= COLLISION_MARGIN_PADDLE:
            game_ball.bounce(bounce_on_y=True, paddle_bounce=True)

        # check for collisions with screen sides
        if abs(game_ball.xcor()) >= WIDTH / 2:
            game_ball.bounce(bounce_on_x=True)

        # check for collisions with screen top
        if game_ball.ycor() >= HEIGHT / 2:
            game_ball.bounce(bounce_on_y=True)

        # check for collisions with screen bottom
        if game_ball.ycor() <= -HEIGHT / 2:
            game_score.reduce_life()
            game_paddle.reset()
            game_ball.reset()

        # check for collisions with bricks
        for brick in game_wall.bricks:
            if brick.distance(game_ball) <= COLLISION_MARGIN_BRICK:
                brick.has_been_hit = True
                game_score.update_score()

                if game_ball.ycor() >= brick.bottom_side:
                    game_ball.bounce(bounce_on_y=True)
                elif game_ball.ycor() <= brick.top_side:
                    game_ball.bounce(bounce_on_y=True)
                elif game_ball.xcor() >= brick.left_side:
                    game_ball.bounce(bounce_on_x=True)
                elif game_ball.xcor() <= brick.right_side:
                    game_ball.bounce(bounce_on_x=True)

        # remove bricks that has been hit
        game_wall.remove_has_been_hit()

        if len(game_wall.bricks) <= 0:
            game_score.next_level()
            screen.clear()
            break

        if game_score.lives <= 0:
            game_on = False

    if not game_on:
        game_score.game_over()
        repeat = screen.textinput("Game Over!", "Press Y to play again. N to quit")
        if repeat.upper() == "Y":
            screen.clear()
        else:
            play_again = False

screen.mainloop()
