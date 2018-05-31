# Now this activity involves transforming the code form activity 1 into the
# "object oriented programming" syntax.



print('Challenge 1 -------------')
# Challenge 1:
# See this class definition? Read it and understand it. Expand it to include
# last_name.


class Patient:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.is_checked_in = False
        self.does_drink = None
        self.does_smoke = None
        self.blood_pressure = None
        self.recommendation = None
        self.diagnosis = None
        self.extra_notes = None

    def print_info(self):
        print('-----PATIENT', self.first_name, self.last_name, '----')
        print('Is checked in:', self.is_checked_in)
        print('Drinks?', self.does_drink)
        print('Smokes?', self.does_smoke)
        print('Blood pressure?', self.blood_pressure)
        print('Diagnosis:', self.diagnosis)
        print('Recommendation:', self.recommendation)

    def check_in(self):
        self.is_checked_in = True

    def ask_for_bool(self, question):
        value = input(question)
        value = value.strip()  # remove excess whitespace
        if not value:
            # No value, means its an empty string, exit
            return False
        value = value.lower()[0]  # get the lowercase first value
        if value == 'y':
            return True
        return False

    def ask_for_int(self, question):
        value = input(question)
        value = value.strip()  # remove excess whitespace
        if not value:
            return 0
        return int(value)

    def nurse_check_up(self):
        self.does_smoke = self.ask_for_bool('Does the patient smoke? ')
        self.does_drink = self.ask_for_bool('Does the patient drink? ')
        self.blood_pressure = self.ask_for_int('Patient blood-pressure? ')


    def doctor_diagnose(self):
        if not self.is_checked_in:
            print('Need to check in first.')
            return
        if not self.blood_pressure:
            print('Patient must visit nurse first')
            return

        if self.does_smoke:
            self.recommendation = 'Quitting smoking.'

        if self.blood_pressure > 180:
            self.diagnosis = 'Hypertension Crisis'
            self.recommendation = 'Immediate treatment in ER'
        elif self.blood_pressure > 140:
            self.diagnosis = 'Stage 2 Hypertension'
        elif self.blood_pressure > 130:
            self.diagnosis = 'Stage 1 Hypertension'

        self.extra_notes = input('Extra physician notes? ')

    # Bonus activity: Use pickle to save and load the given object
    def save(self, filename):
        open_file = open(filename, 'wb+')
        pickle.dump(self, open_file)

    @staticmethod
    def load(filename):
        open_file = open(filename, 'rb')
        return pickle.load(open_file)

eric = Patient('Eric', 'Idle')



print('Challenge 2 -------------')
# Challenge 2:
# Add a new method called "print_info". It should print out all the information
# of the patient. Test it out.

eric.print_info()


print('Challenge 3 -------------')
# Challenge 3:
# Add a new method called "check_in". It should set is_checked_in to be True.

eric.check_in()
eric.print_info()



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


eric.nurse_check_up()
eric.print_info()








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



eric.doctor_diagnose()
eric.print_info()






print('-------------')
# Bonus Challenge:
# Create another method called "save". It should take a filename as an
# argument. The Patient information should get saved to that file. Look up
# "static methods". Make a static method called "load" that will restore the
# Python object.
# Hint: An easy way to do this is with the built-in module "pickle"

# will use Python's "pickle" format for this!
import pickle
eric.save('eric_info.p')
eric_loaded = Patient.load('eric_info.p')
eric_loaded.print_info()
# Quick check that saving and loading works:
assert eric.first_name == eric_loaded.first_name


