# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named lets_start
def lets_start():
    print('Time to code!')
lets_start()


print('Challenge 2 -------------')
# Challenge 2:
# Uncomment the following code. Put the following code into a function. That
# function should have a "name" as a parameter. Invoke it once using your name,
# and once using the name of a student next to you.
def say_hi(name):
    print('Hi', name)

say_hi("Shane")



print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Make sure it works.
#
# Then, modify it in the following way:
# 1. Put it into a function
# 2. Give that function an argument that consists of the valid choices
# (presently, only 'quit'). Have it keep on asking until it gets a valid
# choice.
# 3. Return the option the user selected.
# 4. Add print code to remind the user of the valid choices.

def choice(valid=['quit']):
    answer = input('Choice? ')
    while answer not in valid:
       answer = input('Choice? ')
choice(['hi', 'quit'])

print('-------------')
# Bonus Challenge:
# Using the skills you have learned so far, write a "hang-man" word guessing
# game! We've written some code to get you started. If you are unfamiliar with
# the game "Hangman", look it up, or read the summary below:
# Each turn, the user must choose a letter to guess. Whenever a letter is
# guessed, that letter should be filled in. The player wins when they have
# guessed all the letters. The player loses if they run out of wrong-guesses.



def hang_man(guesses=5):
    import random
    guessed_letters = []
    censored = ''
    c = '_'
    def randword():
        word_file = "/usr/share/dict/cracklib-small"
        WORDS = open(word_file).read().splitlines()
        return random.choice(WORDS)
    def print_word():
        # We'll be learning about for-loops next!
        censored_word = censored
        for letter in word_to_guess:
            if letter not in guessed_letters:
                letter = '_'
            censored_word = censored_word + letter + ' '
        return(censored_word)

    word_to_guess = randword()
    print(word_to_guess)
    print(print_word())

    while guesses > 0:
        print("Guesses: ", guesses)
        guessed_letter = input("Guess a letter: ")
        guessed_letters.append(guessed_letter)
        if guessed_letter not in word_to_guess:
            print("Nope!")
            guesses -= 1
        print(print_word())
        if print_word().replace(' ', '') == word_to_guess:
            guesses = 0
            print("Guesses: ", guesses)
            print("Congratulations! You win!")

hang_man(10)
