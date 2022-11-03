from turtle import Turtle

COLOUR = "yellow"
SCORE_MARGIN = 30
FONT = ("Arial", 16, "normal")

STARTING_LEVEL = 1
STARTING_SCORE = 0
STARTING_LIVES = 5
GAME_LEVEL_LIMIT = 10


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOUR)
        self.speed("fastest")
        self.level = STARTING_LEVEL
        self.score = STARTING_SCORE
        self.lives = STARTING_LIVES
        self.level_limit = GAME_LEVEL_LIMIT
        self.goto(0, (self.getscreen().window_height() / 2 - SCORE_MARGIN))

        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}  Lives Left: {self.lives}  Score: {self.score}", font=FONT, align='center')

    def update_score(self):
        self.score += self.level * self.level
        self.refresh()

    def reduce_life(self):
        self.lives -= 1
        self.refresh()

    def game_over(self):
        self.level = STARTING_LEVEL
        self.score = STARTING_SCORE
        self.lives = STARTING_LIVES

    def next_level(self):
        if self.level < self.level_limit:
            self.level += 1
            self.lives = STARTING_LIVES


