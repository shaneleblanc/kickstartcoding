# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named challenge_1, providing a name.

def challenge_1(name=None):
    print('Hello', name, '!')
challenge_1(name='Jack')



print('Challenge 2 -------------')
# Challenge 2:
# Uncomment the following code. Many of these functions and invocation have
# typos or mistakes. Fix all the mistakes and typos to get the code running.
# When running correctly, it should print dialog from a popular movie.

def func_1(name=None):
    print(name, ':', "I can't feel my body")

def func_2(name=None, other_name=None):
    print(name, ':', other_name, ', listen to me!')

def func_3(quality='best', item='burrito'):
    print('Winning that', item, 'was the', quality, 'thing.')

def func_4(name=None, phrase=None):
    print(name, ':', 'I promise.', phrase, ', Jack.', phrase)


func_1(name='Rose')
func_2(name='Jack', other_name='Rose')
func_3(item='ticket')
func_4(name='Rose', phrase="I'll never let go")


print('Challenge 3 -------------')
# Challenge 3:
# Examine the function written that performs addition. Uncomment the code to
# invoke it. Write another invocation to test it out. Use a similar pattern for
# 5 other operations (subtraction, multiplication, division, exponentiation,
# and modulus)

def addition(a=0, b=0):
    print(a + b)
def multiplication(a=0, b=0):
    print(a * b)
def division(a=0, b=0):
    print(a / b)
def exponentiation(a=0, b=0):
    print(a ** b)
def modulus(a=0, b=0):
    print(a % b)

addition(a=10, b=15)
multiplication(a=10, b=15)
division(a=10, b=15)
exponentiation(a=10, b=15)
modulus(a=10, b=15)









print('Challenge 4 -------------')
# Challenge 4:
# Write a function that has a parameter that accepts a list. Have it keep on
# asking for user input UNTIL that input is something within that list.
# HINT: You'll use "while", "input", and "in" or possibly "not in" (for
# checking inclusion within the list)

def accepts_listo(x=['last', 'of', 'strings']):
    response = None
    while response not in x:
        response = input("are you sure?")


accepts_listo()








#PEP 8


print('-------------')
# Bonus Challenge:
# Write a function that has a dict parameter that is a "menu" of options. This
# dict should have keys that consist of the text that can be entered, and
# values that consist of functions. When the person selects an item from the
# menu, it should execute that function.
#
def menu(options={}):
    response = None
    while response not in options.keys():
        print("Choose from your options: ", options.keys())
        response = input("? ")

    func = options[response]
    func()

def func1():
    print("we did func1!")

def func2():
    print("we did func2!")

menu({'thing1': func1, 'thing2': func2})
