import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


#Choose a random word from our
rand = round(random.random()*len(word_list))-1
chosen_word = word_list[rand]
print(chosen_word)

lives = 6

#create a list that has blanks for each letter in chosen word
display = []

for letter in chosen_word:
    display += '_'

print(display)

while '_' in display:
    #Accept an input from the user to guess a letter
    guess = input('guess a letter ').lower()
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            print('Yay! You got letter ' + guess)
            display[index] = guess


    lives -= 1
    print(guess + ' is not in the word. You have ' + str(lives) + ' lives left.')

    if lives == 0:
        print('Game over.')
        break

    print(display)

print('You win! You got all the letters in ' + chosen_word)
