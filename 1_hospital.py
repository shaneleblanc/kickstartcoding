# REMINDER: Only do one challenge at a time! Save and test after every one.


# For this challenge, we are going to build up a set of functions to create
# code for a semi-realistic situation: We will be building helper functions to
# manage data about a patient at a hospital. You can imagine the final software
# being useful for nurses and doctors to keep track of information on patients.

# The information about patients will be in a dictionary that is passed around
# via parameters to and from functions.

print('Challenge 1 -------------')
# Challenge 1:
# Uncomment and examine the following code. See if you can explain what every
# line is doing.

print('Challenge 2 -------------')
# Challenge 2:
# Rewrite patient_initialize so that it has 2 more arguments: first_name, and
# last_name. Write 2 more invocations of the function to create a patient for
# yourself and the student sitting next to you. Use print statements to confirm
# that your function is working correctly.



# def patient_initialize(patient, first_name, last_name):
#     patient['first_name'] = first_name
#     patient['last_name'] = last_name
#     patient['is_checked_in'] = False
#
# shane = {}
# patient_initialize(shane, 'Shane', 'LeBlanc')
# print(shane)
#
# patient_initialize(shakur, 'Shakur', 'Ahmed')
# print(shakur)

print('Challenge 3 -------------')
# Challenge 3:
# Write a new function called "patient_check_in". This function should take a
# patient dictionary as an argument. and then modify that argument to make
# "is_checked_in" set to be True.
# Again, use print to verify it's working.
def patient_check_in(patient):
    patient['is_checked_in'] = True
shane = {}
#patient_check_in(shane)
print(shane)






print('Challenge 4 -------------')
# Challenge 4:
# Write a new function called "patient_nurse_check_up". It should take a
# patient dictionary as an argument. It should then ask the following
# questions. It can be by using input() and storing the result in separate
# variables or items in the dictionary.
#     1. Does the patient smoke?
#     2. Does the patient drink?
#     3. Patient blood-pressure?
# After each question, it should store that information into the patient
# dictionary.
# Again, use print to verify it's working.

def patient_nurse_check_up(patient):
    patient['smokes'] = input('Does the patient smoke?')
    patient['drinks'] = input('Does the patient drink?')
    patient['bp'] = int(input('Patient blood pressure?'))
    patient['seen_nurse'] = True

#patient_nurse_check_up(shane)

print(shane)





print('Challenge 5 -------------')
# Challenge 5:
# Time to bring it all together. Write a new function called "patient_visit".
# Using inputs, it should ask the name of the patient, then initialize the
# patient with that information. It should then use all of the above functions
# to "process" the patient.
# Hint: Feel free to comment out the previous invocations of the above function
# Add a prints as needed to report back on the process.
def patient_initialize(first_name, last_name):
    patient = {}
    patient['first_name'] = first_name
    patient['last_name'] = last_name
    return patient

def patient_visit():
    patient = patient_initialize(input('First name?'), input('Last name?'))
    patient_check_in(patient)
    patient_nurse_check_up(patient)
    return patient

#print(patient_visit())

print('-------------')
# Bonus Challenge 1:
# Create another function called "patient_doctor_diagnose". It should only
# accept patients who have already been checked in and visited a nurse. It
# should allow a doctor to enter a "diagnosis" and "recommendation".
#
# 1. Check that blood-pressure is below 120. If between 120-130 it should
#    diagnose "Stage 1 Hypertension", if between 130-180 "Stage 2 Hypertension"
# 2. Recommend the patient a) visit the ER if blood pressure is above 180, or
#    b) if the patient smokes, recommend the patient stop.

def patient_doctor_diagnose(patient):
    if patient['seen_nurse'] == True:
        print('Doctor: Hello, ', patient['first_name'])
    if 180 > patient['bp'] > 130:
        print('Doctor: '+ patient['first_name'] + ', this doesn\'t look good... u got stage 2 hypertension')
    if 130 > patient['bp'] > 120:
        print('Doctor: '+ patient['first_name'] + ', it\'s only stage 1 hypertension, smoke on pal')
patient_doctor_diagnose(patient_visit())





print('-------------')
# Bonus Challenge 2:
# Where does our data go? At the end of every check up, we should store it in a
# file. Maybe use JSON, or CSV?
