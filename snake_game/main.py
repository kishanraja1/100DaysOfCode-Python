from turtle import Screen


from snake import Snake



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
snake.move_snake()

screen.exitonclick()