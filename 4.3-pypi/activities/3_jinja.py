# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Examine the following code. See if you can explain what every line is
# doing. Change the name to your name.

from jinja2 import Template

template = Template('Hello, {{ name }}!')
result = template.render(name='Shane')
print(result)


print('Challenge 2 -------------')
# Challenge 2:
# Write the code to utilize this template to render your own name,
# favorite color, favorite food, and favorite book.

from jinja2 import Template

user_information_template = Template('''
<p>Name: {{ name }}</p>
<p>Favorite color: {{ color }}</p>
<p>Favorite food: {{ food }}</p>
<p>Favorite book: {{ book }}</p>
''')
info = user_information_template.render(name='Shane',color='Blue',food='pb',book='something')
print(info)


print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the print function invocation. Only modify the template code
# to add the template variables necessary to categorize the foods (do
# not modify the invocation). The first done is done for you.

template_code = '''
Healthy foods: {{ foods.fruit }}, {{ foods.vegetable }}, {{ foods.cold_dish }}
Junk foods: {{ foods.sandwich }}, {{ foods.drink }}, {{ foods.snack }}
'''


food_template = Template(template_code)
foods = {
    'fruit': 'apple',
    'vegetable': 'carrot',
    'sandwich': 'burger',
    'drink': 'mtn dew',
    'cold_dish': 'salad',
    'snack': 'doritos',
}
print(food_template.render(foods=foods))






print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the print function invocation. By only modifying the
# "context" dictionary, can you figure out how to make this print the
# HTML of a simple website?
# Hint 1: Look for plural / singular as a clue of data types.
# Hint 2: You might find helpful this description of built-in filters:
#  http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters


template_code = '''
<h1>{{ title }}</h1>
<p>My blog posts:</p>
<h2>{{ blog_post_titles|first|title }}</h2>
<h2>{{ blog_posts|first|truncate }}</h2>
'''
context = {
    'title': 'Blog Post',
    'blog_post_titles': ['Hippity doo daa', 'Blibbity blue blah'],
    'blog_posts': ['''This is a
    shit ton of context
    and
    its
    a blog post
    okay??''',
    '''this is the next blog post''']

}

print(Template(template_code).render(context))



print('Challenge 5 -------------')
# Challenge 5:
# Uncomment the print function invocation. Only modify the template code
# adding filters necessary to do the thing it says. The first one is
# done for you, and demonstrates how to comma seperate a list of
# strings using the "join" filter.
# Hint: You'll have to research different filters here:
# http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters


template_code = '''
All noodles: {{ noodles|join(', ') }}
Alphabetical: {{ noodles|sort }}
Reverse alphabetical: {{ noodles|sort(reverse=true) }}
First: {{ noodles|first }}
Last, with a capital letter: {{ noodles|last|title }}
First alphabetically: {{ noodles|sort|first }}
Last alphabetically: {{ noodles|sort|last }}
Number of different types of noodles: {{ noodles|count }}
'''

noodles = [
    'soba',
    'ramen',
    'lo mein',
    'spaghetti',
    'jap chae',
    'vermicelli',
    'gnocchi',
]

print(Template(template_code).render(noodles=noodles))



print('-------------')
# Bonus Challenge:
# Use your jinja2 templating skills to separate the messages of the game
# you worked on at the beginning of today. Put those into Jinja
# templates, and then runb
