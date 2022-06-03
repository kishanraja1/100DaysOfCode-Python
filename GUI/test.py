from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?')
print(user_bet)
tim.penup()
tim.goto(x=-230, y=-100)


screen = Screen()
screen.exitonclick()