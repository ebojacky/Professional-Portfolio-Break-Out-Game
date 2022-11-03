import random
from turtle import Turtle

COLOUR = "yellow"
X_STEP = 10
Y_STEP = 10
X_MARGIN = 0
Y_MARGIN = 100


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.shapesize(0.5, 0.5),
        self.shape("circle")
        self.penup()
        self.window_width = self.getscreen().window_width()
        self.window_height = self.getscreen().window_height()
        self.x_step = X_STEP
        self.y_step = Y_STEP

        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce(self, bounce_on_x=False, bounce_on_y=False, paddle_bounce=False):
        if paddle_bounce:
            # making bounce direction unpredictable
            self.x_step *= random.choice([1, -1])

            # change the bouncing angle by changing y value
            self.y_step = random.choice(range(int(Y_STEP/2), Y_STEP+1)) * -1

        if bounce_on_x:
            self.x_step *= -1

        if bounce_on_y:
            self.y_step *= -1

    def reset(self):
        self.goto(0, -(self.window_height / 2 - Y_MARGIN))

