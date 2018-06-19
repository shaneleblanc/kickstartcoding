# For this activity, we start with a patient pre-created

class Patient:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.is_checked_in = False
        self.does_drink = None
        self.does_smoke = None
        self.recommendation = None
        self.diagnosis = None
        self.extra_notes = None
        self.blood_pressure = 0

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

    def nurse_check_up(self):
        self.does_smoke = input('Does the patient smoke? ') == 'yes'
        self.does_drink = input('Does the patient drink? ') == 'yes'
        self.blood_pressure = int(input('Patient blood-pressure? '))

    def doctor_diagnose(self):
        if not self.blood_pressure:
            print('Patient must visit nurse first')
            return

        if self.blood_pressure > 180:
            self.diagnosis = 'Hypertension Crisis'
            self.recommendation = 'Immediate treatment in ER'
        elif self.blood_pressure > 140:
            self.diagnosis = 'Stage 2 Hypertension'
        elif self.blood_pressure > 130:
            self.diagnosis = 'Stage 1 Hypertension'

        self.extra_notes = input('Extra physician notes? ')



print('Challenge 1 -------------')
# Challenge 1:
# Debugging challenge: Examine the class above. When you uncomment the
# following lines, an error occurs. Instead of saying "Patient must visit nurse
# first", it causes a Python error.  Why is that? Can you fix it?
# HINT: This requires editing the original class.


print('Challenge 2 -------------')
# Challenge 2:
# It's extension time! Here's the challenge: The General Oop Hospital has an
# Emergency Room, and they want patients processed differently. Create a new
# EmergencyPatient class that inherits from the Patient base-class.



class EmergencyPatient(Patient):

    def __init__(self, patient):
        super().__init__(patient.first_name, patient.last_name)
        self.is_checked_in = True


    def triage(self):
        if input('Requires life saving intervention?') == 'True':
            self.triage_level = 1
            return
        if input('Confused, lethargic, severe distress?') == True:
            self.triage_level = 2
            return
        x = input('How many resources needed (none, some, or many):')
        if x == 'none':
            self.triage_level = 5
            return
        if x == 'one':
            self.triage_level = 4
            return
        if x == 'many':
            self.triage_level = 3
            return

    def print_info(self):
        print(super().print_info(), "\n Triage level:", self.triage_level)


eric = Patient('Eric', 'Idle')
ep = EmergencyPatient(eric)
ep.triage()
ep.print_info()



print('Challenge 3 -------------')
# Challenge 3:
# Add to the EmergencyPatient class a "triage" method, that asks the following
# questions, and assigns a number to a "triage_level" property in the following
# manner (in pseudocode):
# - Requires life saving intervention?
#       - yes means triage_level = 1, and triage ends
# - Is high risk: confused, lethargic, severe distress?
#       - yes means triage_level = 2, and triage ends
# - How many resources needed (none, some, or many):
#       - "none" means triage_level = 5, and triage ends
#       - "one" means triage_level = 4, and triage ends
#       - "many" means triage_level = 3, and triage ends






print('Challenge 4 -------------')
# Challenge 4:
# So far so good, but the print_info() method of EmergencyPatient isn't showing
# the new triage_level property. Override print_info() so that it prints out
# triage_level. Use super() to re-use the base class's print_info() method.




print('Challenge 5 -------------')
# Challenge 5:
# The hospital needs all emergency patients to start as is_checked_in by
# default.  Can you override __init__ method in the EmergencyPatient class that
# makes is_checked_in start as True for EmergencyPatients?
# Hint: Use super().__init__(first_name, last_name)







print('-------------')
# Bonus Challenge:
# Look up how to do multiple inheritance in Python. Can you refactor the
# EmergencyPatient into 3 total classes:
# 1. Emergency "mixin"
# 2. Patient "base class"
# 3. EmergencyPatient that derives from both Emergency and Patient.
#
# The EmergencyPatient class should have the triage method, but nothing else.
#
# Why do you think this pattern is useful?




# Bonus Challenge 2:
# Look up the following less common concepts, and see if you can explain them
# in your own words.
# 1. Singleton pattern
# 2. Factory pattern
# 3. Object pool
