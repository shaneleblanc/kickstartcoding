from jinja2 import Template

print('------------- Example 1 - basic templating')
template = Template('''
    Hello, {{ name }}!
    How is your {{ pet }}?
''')

results = template.render(
    name='Joaquin',
    pet='hamster',
)
print(results)


print('------------- Example 2 - dictionaries')


template = Template('''
Accessing Dictionary
Name: {{ patient.name }}
Age: {{ patient.age }}
Blood pressure: {{ patient.blood_pressure }}
''')


patient_info = {
    'name': 'Terry Gilliam',
    'age': 77,
    'blood_pressure': 130,
}
results = template.render(patient=patient_info)
print(results)





print('------------- Example 3 - filters')


template = Template('''
<p>{{ page_title|title }}</p>
<p>Summary: {{ page_text|trim|truncate(60) }}</p>
''')

page_title = 'bRiAn nEEds to cHEEr up'
page_text = '''
Cheer up, Brian. You know what they say, some things in life are bad.
They can really make you mad.  Other things just make you swear and
curse.  When you're chewing on life's gristle, Don't grumble. Give a
whistle.  And this'll help things turn out for the best. And.  Always
look on the bright side of life.
'''
results = template.render(
    page_title=page_title,
    page_text=page_text,
)
print(results)

