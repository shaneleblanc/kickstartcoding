import requests

print('------------ Challenge 1')
# Challenge 1
# Examine the following code. Can you understand what it is doing? As a
# hint, this is the code to use a Studio Ghibli API and fetch
# information about their films. Uncomment the print statement, and get
# it running.


response = requests.get('https://ghibliapi.herokuapp.com/films/')
data = response.json()
# print(data)

print('------------ Challenge 2')
# Challenge 2
# Write code to print out ONLY the "release_date" for "My Neighbor
# Totoro" from the list.
#
# Uncomment this code to get going.
for item in data:
    if item['title'] == 'My Neighbor Totoro':
        print('My Neighbor Totoro release date:', item['release_date'])


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
rates = data['rates']
for code, rate in rates.items():
    print(code, rate)

response = requests.get('https://exchangeratesapi.io/api/latest?symbols=USD')
data = response.json()
usd_rate = data['rates']['USD']
print('USD rate', usd_rate)

response = requests.get('https://exchangeratesapi.io/api/2015-12-31?symbols=EUR&base=USD')
data = response.json()
usd_rate = data['rates']['EUR']
print('USD -> EUR rate on 2015-12-31: ', usd_rate)




print('------------ Challenge 4')
# Challenge 4
# Write a script that uses this Registered Domain Name Search API to
# look for free domain names with your first name, followed by the
# following words, followed by '.com'
words = [
    'dev',
    'webdev',
    'pythonista',
    'coder',
    'hacker',
]

name = 'michael'
free_domains = []
for word in words:
    combo = name + word + '.com'
    try:
        results = requests.get('https://api.domainsdb.info/search?query=' + combo)
        data = results.json()
    except Exception as e:
        # couldn't find it, means it is free!
        free_domains.append(combo)

print('Free domains:', free_domains)




print('------------')
# Bonus Challenge 1
# Use the Yahoo! Weather API to get the weather for Oakland, CA.
# Research the API. Look specifically at
# https://developer.yahoo.com/weather/?guccounter=1




url = (
    'https://query.yahooapis.com/v1/public/yql?q='
    'select%20*%20from%20weather.forecast%20where%20woeid%20in%20'
    '(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'
    'oakland%2C%20ca%22)&format=json&env=store%3A%2F%2Fdatatables.org'
    '%2Falltableswithkeys'
)
response = requests.get(url)
data = response.json()
print('pressure', data['query']['results']['channel']['atmosphere']['pressure'])
print('humidity', data['query']['results']['channel']['atmosphere']['humidity'])



