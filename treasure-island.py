# This is a control flow/if statement exercise.

print('Welcome to Treasure Island')
print('Your mission is to find the Treasure')

choice_1 = input('You are at a crossroad. Left of right?')

if choice_1.lower() == 'right':
    print('You fell into a hole. Game over')
elif choice_1.lower() == 'left':
    choice_2 = input('You are now at a lonely lake. Wait or Swim?')
    if choice_2.lower() == 'wait':
        print('You fell in a hole. game over')
    elif choice_2.lower() == 'swim':
        print('You have found the treasure. Yay!')
    else:
        print('Invalid Choice. Please start over')
else:
    print('Invalid choice. Please start over')
