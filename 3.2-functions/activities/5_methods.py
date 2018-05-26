# REMINDER: Only do one challenge at a time! Save and test after every one.


print('Challenge 1 -------------')
# Challenge 1:
# Uncomment the following code and fix the typos to practice using the list
# methods. If correct, we should see Shrek, Frozen, Titanic in that order.
my_fave_movies = []

my_fave_movies.append('Titanic')
my_fave_movies.append("Frozen")
my_fave_movies.append("Shrek")
my_fave_movies.reverse()
print(my_fave_movies)


print('Challenge 2 -------------')
# Challenge 2:
# Uncomment the following code and fix the typos to practice using dictionary
# methods. It should print out the dictionary keys, the phrase 'No manners!',
# the dictionary values, and then the word SHREK centered in the screen.

# methods. If correct, we should see Shrek, Frozen, Titanic in that order.
user_info = {
    'username': 'shrek',
    'location': 'swamp',
    'friend': 'donkey',
}

print(user_info.keys())
print(user_info.get('manners', 'No manners!'))
print(user_info.values())
print(user_info.get('manners' 'No manners!'))
print(user_info['username'])


print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Modify it using string methods to "sanitize"
# the input.  That is to say, make it so that the user can type in weird
# spellings of yes, such as "YeS", "  yes    " or "YES" to cause the program
# continue.

answer = 'yes'
while answer == 'yes':
   answer = input('Stay in swamp? ').lower()
   # TODO: Sanitize 'answer' variable
print('Leaving swamp...')


print('Challenge 4 -------------')
# Challenge 4:
# The follow is code to create our own class with our own methods. Uncomment
# the code and fix the typos to get it working.
class Ogre:
    def say_name(self):
        print('My name is Shrek')

    def get_friend_name(self):
        return 'Donkey'

    def get_enemy_name(self):
        return 'Lord Farquaad'

shrek = Ogre()
shrek.say_name()
print(shrek.get_friend_name())
print(shrek.get_enemy_name())




print('Challenge 5 -------------')
# Challenge 5:
# Time to get classy! To get more practice with class syntax, create 3 classes:
# One called LordFarquaad, one called PrincessFiona, one called PrinceCharming.
# Each should have 3 methods, each method returning different values.
#             --------------------- --------------------- ----------------------
#            |  LordFarquaad       | PrincessFiona       | PrinceCharming       |
#             --------------------- --------------------- ----------------------
# get_title  | "Lord"              | "Princess"          | "Prince"             |
# get_name   | "Lord Farquaad"     | "Princess Fiona"    | "Prince Charming"    |
# is_villain | True                | False               | True                 |
class LordFarquaad:
    def get_title(self):
        return "Lord"
    def get_name(self):
        return "Lord Farquaad"
    def is_villain(self):
        return True

class PrincessFiona:
    def get_title(self):
        return "Princess"
    def get_name(self):
        return "Princess Fiona"
    def is_villain(self):
        return False

class PrinceCharming:
    def get_title(self):
        return "Prince"
    def get_name(self):
        return "Prince Charming"
    def is_villain(self):
        return True


print('-------------')
# Bonus Challenge 1:
# We'll get more into classes more next week. But until then, uncomment and
# examine the following code. See if you understand what is going on. See if
# you can refactor the 3 classes you defined in Challenge 5 to be a single
# class that takes different inputs to the `__init__` method. Once you have
# done that, see if you can create 3 instances of the class, one for each
# character that you made above.

class Character:
   def __init__(self, name, title, villain):
       self.name = name
       self.title = title
       self.villain = villain

   def get_name(self):
       return self.name

   def get_title(self):
       return self.title

   def is_villain(self):
       return self.villain

PC = Character("Prince Charmin", "Prince", True)
PF = Character("Princess Fiona", "Princess", False)
LF = Character("Lord Farquaad", "Lord", True)
print(PC.get_name())
print(PC.get_title())
print(PC.is_villain())
print(LF.get_name())
print(PF.get_title())
# Advanced Bonus Challenge:
# See if you can rewrite the bonus challenge from 2_functions.py using a class.
# Hint: Use a single class for "Location", then create many instances of that
# class for each location you can go.
