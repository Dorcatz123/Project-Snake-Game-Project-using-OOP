from turtle import Turtle, Screen
import time

#This is the snake class which is basically new turtles being created and it follows the
#previous turtle:
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for i in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            x = 0 - 20 * i
            new_turtle.penup()
            new_turtle.goto(x, 0)
            self.all_turtles.append(new_turtle)

    def extend(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        last_turtle = self.all_turtles[-1]
        new_turtle.goto(last_turtle.position())
        self.all_turtles.append(new_turtle)

#Resets the snake to 3 length snake:
    def reset(self):
        for segment in self.all_turtles:
            segment.goto(1000,1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if int(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)

    def turn_down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def turn_up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)
