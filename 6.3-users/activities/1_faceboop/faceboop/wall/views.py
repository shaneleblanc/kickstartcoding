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

    # Challenge 4: TODO Finish to include name, date joined, and email


def homepage(request):
    # Challenge 5: TODO: Use the finished NewUserForm to add a spot to
    # add new users to the pages/home.html
    context = {
        'users': users,
    }
    return render(request, 'pages/home.html', context)

def feed(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = PostForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # Challenge 3: TODO - Do something here to add the new data
            # from the form to the list of posts.
            # Hint: form.cleaned_data
            return redirect('/feed/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'pages/feed.html', context)


def search(request):
    # Bonus Challenge: TODO - Make this view work! (Also add in
    # search.html page)
    return render(request, 'pages/search.html', context)

