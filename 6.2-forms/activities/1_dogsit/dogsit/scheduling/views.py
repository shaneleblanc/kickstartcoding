from django.shortcuts import render, redirect

import random

from scheduling import test_data

sitters = []

dogs = []


# This code adds in the test data from the separate file, using the
# "extend" method.
sitters.extend(test_data.sitters)


def homepage(request):
    context = {
        'sitters': sitters,
        'dogs': dogs,
    }
    return render(request, 'homepage.html', context)


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




def list_dog(request):
    context = {}

    # Check if we are getting a post request, that means we are receiving a
    # form submission
    if request.method == 'POST':
        # Let's get all the values out of the POST dictionary
        name = request.POST['name']
        date = request.POST['date']
        start_time = request.POST['start_time']
        duration = request.POST['duration']
        breed = request.POST['breed']
        age = request.POST['age']
        notes = request.POST['notes']

        # Randomly select a dog image
        picture = random.choice(test_data.dog_images)

        # Append a new dictionary for this dog being listed
        dogs.append({
            'name': name,
            'picture': picture,
            'date': date,
            'start_time': start_time,
            'duration': duration,
            'breed': breed,
            'age': age,
            'notes': notes,
        })

        # Redirect to homepage to see result
        return redirect('/')

    return render(request, 'list_dog.html', context)
