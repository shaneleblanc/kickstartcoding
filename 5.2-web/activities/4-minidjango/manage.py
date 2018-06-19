from django.urls import path
from django.http import HttpResponse


# View -- This function, called a "view", is the function that will accept an
# incoming request, and return a response. In this case, it is just sending
# back a message in large fonts, but any logic can go in here to conditionally
# send back any sort of response.
links = '''<a href="/contact/">Contact</a><br>
<a href="/about/">About</a><br>
<a href="/hello-world/">Hello World</a><br>'''

def hello_world(request):
    return HttpResponse(links+'<h1>Hello Django World!</h1>')

def contact(request):
    return HttpResponse(links+'<h1>Contact Page!</h1>')

def about(request):
    return HttpResponse(links+'<h1>About page~!!</h1>')
# Routing -- This list is the list of "URL patterns" that Django will try, in
# order, in order to match the incoming request to a function that will handle
# it and return a response.
urlpatterns = [
    path('hello-world/', hello_world),
    path('contact/', contact),
    path('about/', about),
]


# Boilerplate -- Don't worry about understanding anything from here down
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=sys.modules[__name__],
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
