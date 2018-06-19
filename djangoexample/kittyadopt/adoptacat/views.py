from django.shortcuts import render
from django.urls import path


# Create your views here.
def adoption_homepage(request):
    context = {
        'name': 'Shane',
    }
    return render(request, 'adoption_homepage.html', context)
