# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Create 3 variables with your name, your favorite color, and how many hours of
# sleep you got last night. Print out all 3 values using "print".

name = "Shane"
color = "Purple"
sleep = 7
print(f'{name} likes the color {color} and got {sleep} hours of sleep last night')



print('Challenge 2 -------------')
# Challenge 2:
# Create a list of your favorite authors.

authors = ['Bukowski', 'Huxley', 'Shulgin']
print(authors)



print('Challenge 3 -------------')
# Challenge 3:
# Write an "if-statement" to check if the first author on that list is equal to
# "Douglas Adams". If it is, print "Don't panic!". Otherwise, print "Panic!"
if authors[0] is "Douglas Adams":
    print("Don't panic!")
else:
    print("Panic!")

print('Challenge 3 -------------')
# Challenge 4:
# Using "input", create a while loop that keeps on looping until the user says
# "Stop". Have it print back whatever they say each time it loops.
#
resp = input("'Stop' me if you've heard this one before")
while resp != "Stop":
    resp = input("'Stop' me if you've heard this one before")








print('-------------')
# Bonus Challenge:
# Create a chat bot!
# Using a dictionary and a while / input loop, every time a user enters text
# check in the dictionary for a pre-set set of replies (e.g. "hi" responds with
# "hello").
#
responses = {
    'hello': 'hi',
    'sup': 'nm',
    'u high': 'y',
    'hows life': 'good man thanks for asking'
}
response = input("Chat bot online, 'exit' to exit");
while response != exit:
    response = input("Try me again \n:")
    if response in responses:
        print(responses[response])
    else:
        input("I don't know that.")
