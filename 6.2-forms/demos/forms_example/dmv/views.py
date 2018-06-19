from django.shortcuts import render, redirect
from django import forms

registrations = [
    {
        'first_name': 'David',
        'middle_name': 'Michael',
        'last_name': 'Hasselhoff',
    },
]

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    reason_for_visit = forms.MultipleChoiceField(
        choices=[
            ('renewal', 'License renewal'),
            ('apply', 'License application'),
            ('resume', 'Resume application'),
            ('sid', 'State ID'),
        ],
    )
    street_address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)
    visit_date = forms.DateField(widget=forms.SelectDateWidget)

    # Here's how we might support file uploads:
    # uploaded_image = forms.FileField(required=False)


def registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # the data is in cleaned_data, lets add it to our list
            registrations.append(form.cleaned_data)
            return redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'registrations': registrations,
    }

    return render(request, 'registration.html', context)

