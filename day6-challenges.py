#!/bin/python3
# Challenge 1:
# Uncomment the following code. Check that it is correctly creating a file.

open('myfile.txt', 'w').write('Hello file world!')

file = open('myfile.txt', 'w')

file.write("Sports teams!")
file.close()
# Challenge 2:
# First, store in a variable the name of your favorite sports team (or movie).
# Then, write the code necessary to write this data to a file.
file = open('myfile.txt', 'r')
print(file.read())
file.close()
# Challenge 3:
# Using append mode ('a+'), write the names of your favorite sports teams are
# learning in this course. Each language should be written on a separate time.


open('myfile.txt', 'a+').write('Hello file world!')

file = open('myfile.txt', 'r')
print(file.read())
file.close()


# Bonus Challenge 1:
# Write code such that every time you run this script, it will increment file
# the number found in "count.txt" by one.
count = int(open('count.txt', 'r').read()) + 1;
open('count.txt', 'w').write(str(count));

print(open('count.txt', 'r').read())

# Extra Bonus Challenge 2:
# Look up how to do "rot13" cypher. Can you write the code that reads in a
# file, applies rot13, then writes back the result to the same file?
#
import codecs
if __name__ == '__main__':
