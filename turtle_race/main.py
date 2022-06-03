from turtle import Turtle, Screen

red = Turtle(shape='turtle')
red.color("red")
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?')
print(user_bet)
red.penup()
red.goto(x=-230, y=-100)


screen = Screen()
screen.exitonclick()