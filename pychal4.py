print('------------- Challenge 1')
# Challenge 1:
# Write pseudocode (not real code) for the following application description:
# An application that accepts a username and password and checks them against
# known correct values and then will tell the user if they are logged in or
# not.

print("if the user is known and the password is correct, return true")







print('------------- Challenge 2')
# Challenge 2:
# Uncomment the following line of code. Use "print" to say what the user typed
# back at them.
username = input('Username? ')
print(username)
password = input('Password? ')
print(password)





print('------------- Challenge 3')
# Challenge 3
# Read the following Pseudocode:
#   if they gave the username of "AzureDiamond" and a password of "hunter2"
#      print "Logged on!"
#   otherwise
#      print "Incorrect, go away"
#
# Can you write it in Python?
if (username == "AzureDiamond") and (password == "hunter2"):
	print("Logged on!")
else:
	print("Incorrect, go away")





print('-------------')

# Advanced Bonus Challenge
#
# Phase 1:
# Here is your task: Write a "data-entry" Python application that accepts:
# 1) a student name, and
# 2) their grade on a quiz (a number out of 100)
# It then adds their grade to a txt based on their name.

# Phase 2 (THIS ONE IS HARD!):
# Have it first ask "Add grade or get grade?"
# If they type "get", then read the file and compute an average grade
# If they type "add", then follow the above logic

# HINT: First pseudocode this, then work on the actual Python.

print("take student name and grade on quiz out of 100, then add grade to a file based on name")


def gradesApp():
	then = input('Type get to "get" a grade, and "add" to add a grade.')
	if then == 'get':
		name = input('Studen name?')
		file = open(name+'.txt', 'r').readlines()
		grades = []
		for line in file:
			grades.append(int(str(line).replace("\n","")))
		print(grades)
		print(sum(grades) / float(len(grades)))
		gradesApp()
	elif then == 'add':
		name = input('Studen name?')
		grade = input('Grade on the quiz?')
		file = open(name+'.txt', 'a')
		file.write(grade + "\n")
		file.close()
		gradesApp()
	else:
		print("Closing")
		return

	# Challenge 2:
	# First, store in a variable the name of your favorite sports team (or movie).
	# Then, write the code necessary to write this data to a file.
	file = open(name+'.txt', 'r')
	print(file.read())
	file.close()
gradesApp()
