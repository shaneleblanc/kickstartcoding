from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

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
    text = forms.CharField(widget=forms.Textarea)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


def homepage(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)

        if form.is_valid():
            # Create a new user object populated with the data we are
            # giving it from the cleaned_data form
            User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = NewUserForm()

    users = User.objects.all()

    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'pages/home.html', context)


def feed(request):
    if not request.user.is_authenticated:
        # Use Django's built-in "messages" system to us send the user a
        # message that appears on whatever next page they visit
        messages.warning(request, "You need to log in to view the feed")
        return redirect('/')

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = PostForm(request.POST)

        if form.is_valid():
            form.cleaned_data['username'] = request.user.username
            posts.append(form.cleaned_data)
            return redirect('/feed/')

    else:
        # if a GET  we'll create a blank form
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
