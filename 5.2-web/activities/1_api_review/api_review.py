# REMINDER: Only do one challenge at a time! Save and test after every one.


# Challenges 1-4 have to do with data from Here is information about newspapers
# in Oakland, courtesy of Library of Congress' Chronicling America API.
#
# The URL that was used:
# chroniclingamerica.loc.gov/search/titles/results/?terms=oakland&format=json

import json
data = json.load(open('oakland_newspapers.json'))


print('Challenge 1 -------------')
# Challenge 1:
# The top most news-paper is the Oakland Tribune. Here is how we access the
# publisher field of this data. Can you write the code to print out the start
# and end year of the Oakland Tribune?
print(data['items'][0]['publisher'])
print(data['items'][0]['start_year'])
print(data['items'][0]['end_year'])





print('Challenge 2 -------------')
# Challenge 2:
# Inspect the JSON more closely. Not all the newspapers here are actually from
# Oakland, CA! Can you write code that for-loops through the data, getting only
# the truly Oakland newspapers and puts them into a new list?
# Hint: Check for the "County" field and get only the ones in Alameda County
oakland_ca_newspapers = []
for item in data['items']:
    if item['county'] == ['Alameda']:
        oakland_ca_newspapers.append(item['publisher'])
print(oakland_ca_newspapers)

oakland_ca_newspapers = [item['publisher'] for item in data['items'] if item['county'] == ['Alameda']]
print(oakland_ca_newspapers)
print('Challenge 3 -------------')
# Challenge 3:
# Some of the Oakland newspapers have garbage data, with the end year listed as
# 99999. Can you write another for loop that filters out these newspapers?
valid_ca_newspapers = []
for item in data['items']:
    if item['end_year'] != 9999 and item['county'] == ['Alameda']:
        valid_ca_newspapers.append(item['publisher'])
print(valid_ca_newspapers)

valid_ca_newspapers = [item['publisher'] for item in data['items'] if item['end_year'] != 9999 and item['county'] == ['Alameda']]

print('Challenge 4 -------------')
# Challenge 4:
# Only including the valid Oakland California newspapers, can you write code
# that determines the average (mean) length of time in years that the
# publications lasted?
# Hint: Maybe write in pseudocode first.
publication_lengths = []
for item in data['items']:
    if item['end_year'] != 9999 and item['county'] == ['Alameda']:
        length = int(item['end_year']) - int(item['start_year'])
        publication_lengths.append(length)

publication_lengths = [
int(item['end_year'] - item['start_year'])
for item in data['items']
if item['end_year'] != 9999 and item['county'] == ['Alameda']
]


from statistics import mean
print("Average publication length:",mean(publication_lengths),"years")


print('Challenge 5 -------------')
# Challenge 5:
# To get more practice with this alternative for-loop syntax, rewrite Challenge
# 2-4 using list comprehension, if you didn't already use this syntax.




print('-------------')
# Bonus Challenge 1:
# Research the SuredBits API. Can you write code that looks up the personal
# player data of each player of your favorite team? This might require multiple
# requests.
# https://suredbits.com/api/





print('-------------')
# Bonus Challenge 2:
# Take a look at: https://github.com/toddmotto/public-apis
# Which of those public APIs could you get working using requests?
# If you found any really cool ones, show off your results in Chat!
