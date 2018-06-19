# Make one of the following games, in Python, from scratch. If you already
# have created one of these for a previous activity, then choose a
# different one.
#
# All of these games will likely require use of functions, for-loops,
# while loops, variables, lists, dictionaries, inputs, and possibly import
# statements.
#
# Remember to use all tools at your disposal to plan out your code before
# you even begin!  (Remember to use: Pseudocode and state diagrams, and if
# you are doing OOP, class diagrams)
#
#
# 1. Trivia (Easiest)
#     - Make a trivia game! You have the skills to do this. It should ask
#       a series of questions, such as about capitals of countries.
#     - It should keep track of wrong answers
#     - Stages
#         1: Get 1 question working.
#         2: Get 2 questions working.
#         3: Refactor, so that it randomly selects questions (use the
#         `random` module)
#
# 2. Anagrams
#     - Make an anagrams game, where the player must attempt to
#       "unscramble" the letters in a word.
#     - This game must display a word, except the letters will be
#       scrambled in a random order
#     - The user must then type in what they think the word is. They win
#       if they type in the right one.
#     - HINT: Use the "random" module to shuffle words
#     - BONUS: Can you make it chose a random word each time?
#     - BONUS 2: Can you give it a time limit? (This is actually quite
#       hard)
#
#
# 3. Hangman
#     - Make a hangman game. If you feel stuck starting from scratch, see
#       the bonus activity from last lesson.
#     - While the final application should pick a random word each time,
#       during development, have it use the same word over and over, for
#       testing.
#     - At first, it will only show the word as a bunch of underscores,
#       like "_ _ _ _ _"
#     - Each time the user guesses, it should replace the correct letters
#       with the guessed letter
#     - Focus on getting the basics working first before thinking about
#       winning or losing!
#
#
#
# 4. Bonus: RPG Battle (no solution)
#     - If you have played an RPG game, such as a Pokemon game, you will
#       know there is a "turn based" battle system, where you must face
#       off against an opponent, and are given various strategic choices
#       on each turn.
#     - It must keep track of your health, your magic or ability points,
#       and you must have one or two attack options, and the ability to
#       defend
#     - The opponent must attack each turn, or use some other ability.
#       This will hurt your character by subtracting health from the
#       health variable.
#     - If the player character's health is 0, they lose
#     - If the enemy's health goes down to 0, then the user wins
#     - If you have time, add the ability to "level up" your character.
#       Your character should grow in power after every round, and maybe
#       be able to challenge one opponent after another.
#
# Class Player has HP, AP, and abilities
# Class Ability has different attacks or abilities
#  randomize opponent ability and ask for input for player Ability
#  functions: checkHealth, checkXP
#
player1 = {
    'name': '',
    'hp': 100,
    'ap': 10,
    'abilities': ['attack', 'taunt', 'lightning bolt', 'potion'],
    'power': 5
}
player2 = {
    'name': 'CPU Opponent',
    'hp': 60,
    'ap': 10,
    'abilities': ['attack', 'weaken', 'defend', 'potion'],
    'power': 5
}
player_turn = true
def use_ability(ability,source,target):
    if not player_turn:
        #gen random ability for CPU
        #

def new_game():
    player1['name'] = input("What is your name?")

    battle()

def battle():
    print(f"{player1['name']} encountered {player2['name']}!")

new_game()
