from django.shortcuts import render, redirect
from django import forms

users = [
    {
        "name": "Chun-Li",
        "image": "https://i.imgur.com/bYSjhZe.png",
        "email": "chunli@email.link",
        "password": "hadouken",
        "date_joined": "2000-08-24",
        "username": "just4kicks",
    },
    {
        "name": "Squidward",
        "image": "https://i.imgur.com/QUo3ZVw.png",
        "email": "squid@bikini.bottom",
        "password": "frycooknolonger",
        "date_joined": "2002-03-14",
        "username": "mrtentacles",
    },
]


posts = [
    {
        'username': 'mrtentacles',
        'text': '''
            That's it mister! You just lost your brain privileges!  You're
            a man now, Spongebob, and it's time you started acting like
            one. The maniacs in the mailbox. The sky had tartar sauce.
            Spongebob is the only guy I know who can have fun with a
            jellyfish, for twelve hours. The line for the tunnel of glove
            is filling up. go out and get yourself a case of the krabbies.
            Mr. Krabs, please. I'll prove I'm a fry cook.  Hey look, a
            cardboard box washed up on the beach. Holy fish paste!
        ''',
    },
    {
        'username': 'chunli',
        'text': '''
            Veggies, proinde vos postulo esse magis sierra leone bologi garlic
            beetroot rock melon parsley soybean courgette green bean mung bean
            desert raisin bitterleaf avocado sweet pepper.
        ''',
    },
]

class PostForm(forms.Form):
    username = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    image = forms.URLField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    name = forms.CharField(max_length=100)
    date_joined = forms.DateField(widget=forms.SelectDateWidget)
    email = forms.EmailField()

def homepage(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = NewUserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            users.append(form.cleaned_data)
            return redirect('/feed/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()


    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'pages/home.html', context)

def feed(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = PostForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            posts.append(form.cleaned_data)
            return redirect('/feed/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'pages/feed.html', context)


def _normalize(text):
    '''
    Normalize the given text by making it lower case and removing spaces.
    '''
    return text.lower().replace(' ', '')

def search(request):
    term = ''
    found_posts = []

    if 'query' in request.GET:
        # Normalize the term by making it lower case and replacing all spaces
        # with empty string
        term = request.GET['query']
        term_normalized = _normalize(term)
        if term_normalized:
            found_posts = [
                post for post in posts
                if term_normalized in _normalize(post['text'])
            ]

    context = {
        'term': term,
        'posts': found_posts,
    }
    return render(request, 'pages/search.html', context)

