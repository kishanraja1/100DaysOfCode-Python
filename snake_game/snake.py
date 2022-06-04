from turtle import Screen, Turtle
import time

class Snake:
    def __init__(self):
        self.name = 'Peter'



    def move_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        segments = []

        for position in starting_positions:
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(position)
            segments.append(new_snake)

        game_is_on = True
        while game_is_on:
            Screen().update()
            time.sleep(.1)
            for seg_num in range(len(segments) - 1, 0, -1):
                new_x = segments[seg_num - 1].xcor()
                new_y = segments[seg_num - 1].ycor()
                segments[seg_num].goto(new_x, new_y)
            segments[0].forward(10)
