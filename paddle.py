from turtle import Turtle

COLOUR = "yellow"
SIZE = (10, 1)
SIDE_STEP = 50
X_MARGIN = 0
Y_MARGIN = 100


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.shapesize(SIZE[0], SIZE[1])
        self.shape("square")
        self.window_width = self.getscreen().window_width()
        self.window_height = self.getscreen().window_height()
        self.penup()

        self.reset()
        self.setheading(90)

    def move_ship_left(self):
        if self.xcor() > -(self.window_width / 2):
            self.setheading(180)
            self.forward(SIDE_STEP)
            self.setheading(90)

    def move_ship_right(self):
        if self.xcor() < (self.window_width / 2):
            self.setheading(0)
            self.forward(SIDE_STEP)
            self.setheading(90)

    def reset(self):
        self.goto(0, -(self.window_height / 2 - Y_MARGIN))

