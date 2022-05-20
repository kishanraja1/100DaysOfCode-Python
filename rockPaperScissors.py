import random

options = ['rock', 'paper', 'scissors']

#Player making a choice
player_choice = input('What do you choose? 0 for Rock, 1 for paper, 2 for scissors: ')

player_choice = options[int(player_choice)]


#Computer making a choice
computer_choice = round(random.random()*3)
print(computer_choice)

computer_choice = options[computer_choice]

#Game logic comparing player choice to computer choice
if player_choice == computer_choice:
    print('Its a tie')
elif player_choice == 'rock':
    if computer_choice == 'paper':
        print('computer wins.')
    elif computer_choice == 'scissors':
        print(' player wins.')
elif player_choice == 'paper':
    if computer_choice == 'rock':
        print('player wins')
    elif computer_choice == 'scissors':
        print('computer wins')
elif player_choice == 'scissors':
    if computer_choice == 'rock':
        print('Computer wins')
    elif computer_choice == 'paper':
        print('player wins')



#Output result
print('Player chose ' + player_choice + ' and computer chose ' + computer_choice)
