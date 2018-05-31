# Welcome to General Hospital Oop! Now this activity involves transforming the
# code form activity 1 into the "object oriented programming" syntax.



print('Challenge 1 -------------')
# Challenge 1:
# See this class definition? Read it and understand it. Expand it to include
# last_name.


class Patient:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = 'Idle'
        self.is_checked_in = False


eric = Patient('Eric')



print('Challenge 2 -------------')
# Challenge 2:
# Add a new method called "print_info". It should print out all the information
# of the patient. Test it out.



print('Challenge 3 -------------')
# Challenge 3:
# Add a new method called "check_in". It should set is_checked_in to be True.






print('Challenge 4 -------------')
# Challenge 4:
# Write a new method called "nurse_check_up".
# It should then ask the following questions. It can be by using input() and
# storing the result in separate properties of the patient object.
#     1. Does the patient smoke?
#     2. Does the patient drink?
#     3. Patient blood-pressure?




print('Challenge 5 -------------')
# Challenge 5:
# Refactor the above method to use two other methods: "ask_for_int" and
# "ask_for_bool". These should more intelligently convert whatever the user
# types in into the correct data type. For example, "ask_for_bool" should look
# for "yes" or "no", and convert that to True or False.








print('Challenge 6 -------------')
# Challenge 6:
# Create another method called "doctor_diagnose". It should only work on
# patients who have already been checked in and visited a nurse. It should
# allow a doctor to enter a "diagnosis" and a "recommendation". These are more
# properties added to the Patient class. Make sure the patient starts with a
# diagnosis and recommendation of None when initialized, but later gets it
# filled in by this method. This diagnosis method should do the following:
#
# 1. Check that blood-pressure is below 120. If between 120-130 it should
#    diagnose "Stage 1 Hypertension", if between 130-180 "Stage 2 Hypertension"
# 2. Recommend the patient a) visit the ER if blood pressure is above 180, or
#    b) if the patient smokes, recommend the patient stop.






print('-------------')
# Bonus Challenge:
# Create another method called "save". It should take a filename as an
# argument. The Patient information should get saved to that file. Look up
# "static methods". Make a static method called "load" that will restore the
# Python object.
# Hint: An easy way to do this is with the built-in module "pickle"







