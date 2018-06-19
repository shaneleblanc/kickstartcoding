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
    username = forms.CharField(max_length=100)
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

    users = Users.objects.all()

    # Challenge 3: TODO Add code here to fetch users from the database

    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'pages/home.html', context)


def feed(request):
    # Bonus Challenge: TODO Prevent unauthenticated users from accessing
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to do this.")
        return redirect('/')

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = PostForm(request.POST)

        if form.is_valid():
            # Challenge 5: TODO Make the username always get pulled from
            # the currently authenticated user
            form.cleaned_data['username'] == request.user.username
            posts.append(form.cleaned_data)
            return redirect('/feed/')

    else:
        # if a GET we'll create a blank form
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
