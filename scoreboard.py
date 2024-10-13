from turtle import Turtle

INITIAL_SCORE = 0
INCREMENT_SCORE = 1
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.goto(0,280)    
        self.hideturtle()    
        self.reset_score()
        
    def increment_score(self):
        self.score += INCREMENT_SCORE
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def reset_score(self):
        self.score = INITIAL_SCORE
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)