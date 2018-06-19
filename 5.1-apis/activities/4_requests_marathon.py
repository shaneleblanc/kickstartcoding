import requests

print('------------ Challenge 1')
# Challenge 1
# Examine the following code. Can you understand what it is doing? As a
# hint, this is the code to use a Studio Ghibli API and fetch
# information about their films. Uncomment the print statement, and get
# it running.


response = requests.get('https://ghibliapi.herokuapp.com/films/')
data = response.json()
#print(data)

print('------------ Challenge 2')
# Challenge 2
# Write code to print out ONLY the "release_date" for "My Neighbor
# Totoro" from the list.
#
# Uncomment this code to get going.
for item in data:
   if item['title'] == "My Neighbor Totoro":
       print(item['release_date'])




print('------------ Challenge 3')
# Challenge 3
# Read the API documentation for the Exchange Rates API provided by the
# European Central Bank. Information here: https://exchangeratesapi.io/
# Print out the following information:

# 1. All top conversions between Euros and others
# 2. The cost of 1 USD in Euros today.
# 3. The cost of 1 Euros in USD on the last day of 2015: 2015-12-31
response = requests.get('https://exchangeratesapi.io/api/latest')
data = response.json()
print(data)

response = requests.get('https://exchangeratesapi.io/api/latest?base=USD')
data = response.json()
print(data)

response = requests.get('https://exchangeratesapi.io/api/2015-12-31?symbols=USD,GBP')
data = response.json()
print(data)
print('------------ Challenge 4')
# Challenge 4
# Write a script that uses this Registered Domain Name Search API to look for
# *free domain* names with your first name, followed by the following words,
# followed by '.com'. For example, if your name was 'Joan', one might be
# 'joanhacker.com'.
#
# Hint: You will need to use try/except for this one.
# This is trickier than you might think!
words = [
    'dev',
    'webdev',
    'pythonista',
    'coder',
    'hacker',
]


results = []
for word in words:
    try:
        response = requests.get(f"https://api.domainsdb.info/search?query={word}.com")
        data = response.json()
        results.append(data)
        print(f"Domain exists: {data[0]['domain']}")
    except Exception as e:
        print(f"Did not find the domain : Shane{word}.com", e)
print(results)


print('------------')
# Bonus Challenge 1
# Use the Yahoo! Weather API to get the weather for Oakland, CA.
# Research the API. Look specifically at:
# https://developer.yahoo.com/weather/?guccounter=1
# Can you get the current pressure and humidity?

yahoo = requests.get("https://query.yahooapis.com/v1/public/yql?q=select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text ='Oakland') and u='c'&format=json")
resp = yahoo.json()

print(f"The weather in Oakland is {resp['query']['results']['channel']['item']['condition']['temp']} °C")
# Bonus Challenge 2:
# Take a look at: https://github.com/toddmotto/public-apis
# Which of those public APIs could you get working using requests?
# If you found any really cool ones, show them off!
#
