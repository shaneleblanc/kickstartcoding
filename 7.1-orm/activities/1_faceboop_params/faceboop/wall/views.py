from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from .models import WallPost

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
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )

            # As soon as our new user is created, we make this user be
            # instantly "logged in"
            auth.login(request, user)
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = NewUserForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/home.html', context)


def all_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'pages/user_list.html', context)



def user_feed(request, username):
    # Challenge 2 + 3: Experiment with how this works. See how username that
    # you put in the URL turns into this parameter? Examine also the
    # commented-out code.
    print('This is the username in the URL:', username)

    # user = User.objects.get(username=username)

    context = {
        'username': username,
    }
    return render(request, 'pages/feed.html', context)



def view_city(request, city_name):
    # Challenge 4: Can you use the city_name here to show in the template? Also
    # have to update the urls.py.
    context = {
    }
    return render(request, 'pages/TODO FIX THIS', context)

