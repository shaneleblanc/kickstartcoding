from django.shortcuts import render, redirect

import random

from scheduling import test_data

sitters = []

dogs = []


# Add in the test sitter data we have in test_data
sitters.extend(test_data.sitters)

def homepage(request):
    context = {
        'sitters': sitters,
        'dogs': dogs,
    }
    return render(request, 'homepage.html', context)


def book(request):

    # Get the GET value of the dog we want to book, and convert that to an
    # actual number (instead of a string containing the digits of the number)
    dog_index_string = request.GET['dog']
    dog_index_int = int(dog_index_string)
    dog = dogs[dog_index_int]
    print('found dog:', dog)

    # Create a context with available sitters and the dog we want to book)
    context = {
        'sitters': sitters,
        'dog': dog,
    }

    # If they submitted the form then we should register the dog as being
    # booked, and that the specified sitter is the one who booked it, then
    # return to the homepage
    if request.method == 'POST':
        sitter = request.POST['sitter']
        dog['booked'] = True
        dog['booked_sitter'] = sitters[sitter]
        return redirect('/')

    # Finally, render the appointment confirmation page
    return render(request, 'confirm_appointment.html', context)



def list_sitter(request):
    context = {}

    # Check if we are getting a post request, that means we are receiving a
    # form submission
    if request.method == 'POST':
        # Let's get all the values out of the POST dictionary
        age = request.POST['age']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']

        # For now, just use test-data photos
        picture = "http://placehold.it/150x150"

        # Now, we should append a new dictionary for this sitter being listed
        sitters.append({
            'age': age,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'address': address,
            'picture': picture,
        })

        # Redirect to homepage to see result
        return redirect('/')


    return render(request, 'list_sitter.html', context)


from django import forms

class AppointmentForm(forms.Form):
    # Add in more...
    name = forms.CharField(label='Name', required=True)
    age = forms.IntegerField(label='Age', required=True)
    breed = forms.CharField(label='Breed', required=True)
    notes = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.SelectDateWidget)
    duration =  forms.ChoiceField(widget=forms.RadioSelect, choices=[
            (15, '15 minutes'),
            (30, '30 minutes'),
        ],
    )
    start_time = forms.TimeField(label='Start time')

def list_dog(request):
    # Let's start with "no error", but then if something wasn't filled out
    # right, we'll have to add it in here
    # Check if we are getting a post request, that means we are receiving a
    # form submission
    form = AppointmentForm()
    if request.method == 'POST':
        # Let's get all the values out of the POST dictionary
        form = AppointmentForm(request.POST)

        if form.is_valid():
            dogs.append(form.cleaned_data)
            return redirect('/')

        else:
            form = AppointmentForm()


    context = {
        'error': None,
        'form': form,
    }
    return render(request, 'list_dog.html', context)
