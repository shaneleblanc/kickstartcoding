# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named challenge_1

def challenge_1():
    print('Hello Functional World!')

challenge_1()

print('Challenge 2 -------------')
#Challenge 3:
#Uncomment the following code. Many of these functions and invocations have
#typos or mistakes. Fix all the mistakes and typos to get the code running.
#When running correctly, it should say a b c d on separate lines.

def func_1():
    print("a")

def func_2():
    print("b")

def func_3():
    print("c")

def func_4():
    print("d")


func_1()
func_2()
func_3()
func_4()






print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Make sure it works. See how repetitive it is?
# See if you can "refactor" it to be less repetitive. This will require putting
# the repetitive bits of the code into a function, then invoking the function
# in lieu of repeating the code.
# print("We need to ask your name 3 times.")
# name = input('What is your name? ')
# print("Hi", name)
# name = input('What is your name? ')
# print("Hi", name)
# print("And one more time....")
# name = input('What is your name? ')
# print("Hi", name)

print("We need to ask your name 3 times.")
def askName():
    name = input('What is your name? ')
    print("Hi", name)
askName()
askName()
print("And one more time....")
askName()



print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the following code for a text-based videogame. Can you understand
# what it is doing, and how you can get it working? Follow the same pattern to
# add a function that includes a hallway scene.

def bedroom():
    print('You are in a bedroom. A window is open and the sun is shining in.')
    print('There is a cell phone, resting on top of a chest of drawers.')
    print('north: Hallway')
    print('south: Bathroom')
    choice = input('? ')
    if choice == 'north':
        hallway()
    elif choice == 'south':
        bathroom()
    else:
        bedroom()

def bathroom():
    print('You are in a small bathroom. Everything is sparkling clean, except')
    print('there is toothpaste smeared on the counter. One small window lets')
    print('a bright beam of sunshine in.')
    print('north: Bedroom')
    choice = input('? ')
    if choice == 'north':
        bedroom()
    else:
        bathroom()

def hallway():
    print('''You are in a long hallway, seemingly stretching further than than the depths of your mind
You feel pain looking at the pictures, lost lives and lovers, hanging on the wall
south: Bedroom
north: Further down

    ''')
    choice = input('?')
    if choice is 'south':
        bedroom()
    else:
        hallway()

bedroom()

print('-------------')
# Bonus Challenge:
# Make it so that you can take the phone while in the bedroom with a command
# "take phone", and once picked up. Once picked up, make it so that the phone
# will "start ringing" after traveling to a few different rooms. If you have
# more time... have that phone call begin a mystery puzzle!
# HINT: You will probably need to use variables to mark that you have the
# phone, among other things. Look the "global" keyword in Python, it might come
# in handy.
