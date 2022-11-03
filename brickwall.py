import random
from turtle import Turtle

COLOURS = ["#9D5C0D", "#C56824", "#8E3200", "#A64B2A", "#8E3200", "#A64B2A", "#632626", "#9D5353"]

X_MARGIN = 100
Y_MARGIN = 100
BRICK_GAP = 2
BRICK_SIZE = 21


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLOURS))
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.left_side = self.xcor() - BRICK_SIZE
        self.right_side = self.xcor() + BRICK_SIZE
        self.top_side = self.ycor() + BRICK_SIZE/2
        self.bottom_side = self.ycor() - BRICK_SIZE/2
        self.has_been_hit = False


class BrickWall(Turtle):
    def __init__(self, game_level):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.window_width = self.getscreen().window_width()
        self.window_height = self.getscreen().window_height()
        self.no_of_layers = 2 * game_level

        self.create_wall()

    def create_wall(self):
        starting_position_per_row = []

        for i in range(self.no_of_layers):
            pos = (-(self.window_width / 2 - X_MARGIN),
                   (self.window_height / 2 - Y_MARGIN) - i * (BRICK_SIZE + BRICK_GAP))
            starting_position_per_row.append(pos)

        for ind, pos in enumerate(starting_position_per_row):
            if ind % 2 == 0:
                pos = (pos[0] + (BRICK_SIZE + BRICK_GAP), pos[1])

            j = 0
            while True:
                x = pos[0] + j * 2 * BRICK_SIZE + BRICK_GAP
                y = pos[1]

                if x >= self.window_width / 2 - X_MARGIN:
                    break

                new_brick = Brick()
                new_brick.goto(x, y)
                self.bricks.append(new_brick)
                j += 1

    def remove_has_been_hit(self):
        for item in self.bricks:
            if item.has_been_hit:
                item.hideturtle()
                self.bricks.remove(item)
