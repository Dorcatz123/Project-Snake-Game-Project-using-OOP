from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 12, "normal")

#Keeps track of score board:
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = None
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.points = 0
        self.read_highscorefile()
        self.goto(0,280)
        self.update_score()
        self.hideturtle()

#Use opwn file command to read previous score or update high scores:
    def read_highscorefile(self):
        #with open("C:\\Users\\aksha\\OneDrive\\Desktop\\data", "r") as file:
        with open("../../PycharmProject/snake_game/data", "r") as file:
            self.high_score = int(file.read())

    def update_highscore(self):
        with open("C:\\Users\\aksha\OneDrive\\Desktop\\data", "w") as file:
            file.write(f"{self.high_score}")


    def reset(self):
       if self.points > self.high_score:
            self.high_score = self.points
            self.update_highscore()
       self.points = 0

#Updates scores in the turtle screen
    def update_score(self):
          self.clear()
          self.write(f"Score: {self.points} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score(self):
        self.points += 1
        self.update_score()

