#!/bin/python3
print("Hello World!")
print("""
Fever
By Hailey Leithauser
The heat so peaked tonight
the moon can’t cool

a scum-mucked swimming
pool, or breeze

emerge to lift the frowsy
ruff of owls too hot

to hoot, (the mouse and brown
barn rat astute

enough to know to drop
and dash) while

on the bunched up,
corkscrewed sheets of cots

and slumped brass beds,
the fitful twist

and kink and plead to dream
a dream of air

as bitter cruel as winter
gale that scrapes and blows

and gusts the grate
to luff

the whitened ashes from the coal.
""")

print("ABCDZ" * 12 + '3');
print(10000 - (15325 * 14 - (50 ** 10))** 15)
print("Five times whatever" * 5 );
print('2+ 2 is a string');
name = "George"
age = 106

print('{} is {} years old'.format(name,age))
print('You should know this fact, {name}: {fact} \n {fact}, {name}!'.format(fact='"Things happen."',name=name))

print(f'Name: {name} Age: {age}')

print('The %s is %i years old' % (name, age))

print('Hello %(name)s - you are %(age)i years old. Damn, %(name)s' % {'name': name, 'age': age})


spam = 100
eggs = 200

menu = spam + eggs
print(menu)
questions_remaining = 3
name = 'King Arthur'
average_velocity_of_swallow = 38.6243
is_parrot_dead = True
cheese_left_in_shop = None
print("Type of questions_remaining:", type(questions_remaining))
print("Type of name:", type(name))
print("Type of average_velocity_of_swallow:", type(average_velocity_of_swallow))
print("Type of is_parrot_dead:", type(is_parrot_dead))
print("Type of cheese_left_in_shop:", type(cheese_left_in_shop))

number = 0; number = number + 1; print(number)

print('Challenge 6: b will print 5')

print('---------------')
# Advanced Challenge 1: Unpacking Assignment
# Uncomment the following lines and use print to output the contents of the
# variables to get an idea of what is happening. Try the top input on the
# bottom split.
a, b = 1, 2
name = "Dominic Monaghan"
first_name, last_name = name.split()
name = "Dominic Bernard Patrick Luke Monaghan"
first_name, *middle_names, last_name = name.split()
print(name);
print(first_name);
print(last_name);

# Advanced Challenge 2: Advanced Unpacking Assignment
# Uncomment the following lines. Only by replacing the ?????????, make the
# following print statement print out 0, 1, 2, 3, 4, 5, 6, 7
nested = (0, (1, (2, 3), 4, 5), 6, 7)
a, (b, (c, d), e, f), g, h = nested
print(a, b, c, d, e, f, g, h)

##Final question: Do you think this advanced unpacking "Pythonic" or not?
#Yes
print( 10 / 100)
print ( 10 // 100 )
import subprocess;

test = open('~/projects/portfolio/templates/top.html');
