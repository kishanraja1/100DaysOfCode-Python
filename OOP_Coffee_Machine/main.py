# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue", "cyan")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
#
# table = PrettyTable()
# table.field_names = ["Pokemon", "Type"]
# table.add_row(["Mewtew", "Magic"])
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Charmander", "water"])
# table.align = 'l'
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Create objects from our classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



user_input = input('What would you like to order? ')

def coffee_machine(user_input):
    if(user_input == 'off'):
        print('turning off')
        return
    elif(user_input == 'report'):
        money_machine.report()
        coffee_maker.report()


coffee_machine(user_input)