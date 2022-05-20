import random

options = ['rock', 'paper', 'scissors']

#Player making a choice
player_choice = input('What do you choose? 0 for Rock, 1 for paper, 2 for scissors: ')

player_choice = options[int(player_choice)]


#Computer making a choice
computer_choice = round(random.random()*3)

computer_choice = options[computer_choice])
