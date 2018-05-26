# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named challenge_1

def challenge_1():
    print('Hello Functional World!')
challenge_1()


print('Challenge 2 -------------')
# Challenge 3:
# Uncomment the following code. Many of these functions and invocations have
# typos or mistakes. Fix all the mistakes and typos to get the code running.
# When running correctly, it should say a b c d on separate lines.

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

def ask_name():
    name = input('What is your name? ')
    print("Hi", name)

print("We need to ask your name 3 times.")
ask_name()
ask_name()
print("And one more time....")
ask_name()


print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the following code for a text-based videogame. Try to analyze what
# it does. Can you get it working? Expand it to include a hallway scene.


print('-------------')
# Bonus Challenge:
# Make it so that you can take the phone while in the bedroom with a command
# "take phone", and once picked up. Once picked up, make it so that the phone
# will "start ringing" after traveling to a few different rooms. If you have
# more time... have that phone call begin a mystery puzzle!
# HINT: You will probably need to use variables to mark that you have the
# phone, among other things. Look the "global" keyword in Python, it might come
# in handy.

phone_call = 5
has_phone = False
def bedroom():
    if has_phone:
        check_phone()

    print('You are in a bedroom. A window is open and the sun is shining in.')
    if not has_phone:
        print('There is a cell phone, resting on top of a chest of drawers.')
    print('north: Hallway')
    print('south: Bathroom')
    choice = input('? ')
    if choice == 'north':
        hallway()
    elif choice == 'south':
        bathroom()
    elif choice == 'take phone':
        global has_phone
        has_phone = True
        bedroom()
    else:
        bedroom()

def bathroom():
    if has_phone:
        check_phone()

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
    if has_phone:
        check_phone()

    print('You are in a narrow hallway. There is a door locked to the north.')
    print('north: Locked door')
    print('south: Bedroom')
    choice = input('? ')
    if choice == 'south':
        bedroom()
    elif choice == 'north':
        print("Try as you may, you can't force the door open.")
        hallway()
    else:
        hallway()

def check_phone():
    global phone_call
    phone_call = phone_call - 1
    if phone_call == 0:
        print('The phone starts vibrating. Do you answer it?')
        choice = input('? ')
        if choice == 'yes':
            print()
            print('You answer the call. Your vision starts closing in.')
            print('You hear a grave voice from the phone rasp, "Now it begins..."')
            print('You black out.')
            print()
            print('To be continued!')
            print()
            print('------------------------------')

# To get it going!
bedroom()
