from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context

# Our different "view" functions
def index(request):
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
    ''')

def about_me(request):
    return HttpResponse('''
        <h1>About me</h1>
    ''')

# Routing: Set up which URLs we are looking at, with which functions will be
# called to handle this URL
urlpatterns = [
    path('', index),
    path('about-me', about_me),
]


# Boilerplate -- Don't worry about understanding anything from here down
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=sys.modules[__name__],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }],
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

