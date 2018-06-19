import requests

print('------------ Challenge 1')
# Challenge 1
# Examine the following code. Can you understand what it is doing? Can
# you predict the sort of data it will print out? Get it functioning.
# You will need to use pipenv to install requests.
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_code = response.text
for line in html_code.splitlines():
    if 'Harry R. Truman' in line:
        print(line)





print('------------ Challenge 2')
# Challenge 2
# Go to the website in your browser.  Using the top code as a guide,
# write code that will look for the topic of today's featured article,
# and print out the text surrounding that.









print('------------ Bonus Challenge')
# Bonus Challenge:
# Take a look at: https://github.com/toddmotto/public-apis
# Which of those public APIs could you get working using requests?
# If you found any really cool ones, show them off!
