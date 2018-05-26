# REMINDER: Only do one challenge at a time! Save and test after every one.


print('Challenge 1 -------------')
# Challenge 1:
# The following function and invocation have some typos. Uncomment the lines,
# then fix them to get it running.

def comma_name(first_name, last_name):
   return(last_name + ", " + first_name)
author_name = comma_name('William', 'Shakespeare')
print(author_name)



print('Challenge 2 -------------')
# Challenge 2:
# 1. Write a function called "prepare_greeting". It should combine the string
# "Hello " followed with a name supplied as an argument.
# 2. Write the functions invocation. Take the return value and put it into a
# variable. Once in the variable, it should print out the result.
def prepare_greeting(name):
    return f"Hello {name}"

greeting = prepare_greeting("Sam")
print(greeting)

print('Challenge 3 -------------')

# Challenge 3:
# Context: In geometry, the square-root of the sum of two squares determines
# the length of a line. This is called the "Pythagorean theorem".
# Write a function called "get_length" that calculates the Pythagorean theorem
# and returns the value. Invoke it for each of the following pairs, storing
# each result in a variable, and printing out the result:
# 3 and 5
# 2 and 2
# 10 and 61
# Note: It *should not* just print the value, but instead return the value.
# Hint: "2 ** 0.5" gets the square root of 2
def get_length(num1, num2):
    return (num1 + num2) ** 0.5

print(get_length(3, 5))




print('-------------')
# Bonus Challenge:
# Write a function that calculates if a given value is a prime number. Prime
# numbers are numbers that are evenly divisible only by themselves and 1,
# nothing else. The first few prime numbers are: 2, 3, 5, 7, 11, and 13.
# The function should be called "is_prime" and return True if the given number
# is_prime, and False if it is not.
# Hint: To check if a number is evenly divisible by another, you can use the
# following snippet:
# if 6 % 3 == 0:
#    print('3 goes into 6 evenly!')

# Double bonus: What ways can you improve it to run faster?
def is_prime(num):
    divisor = 2
    while divisor != num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

print(is_prime(13))
