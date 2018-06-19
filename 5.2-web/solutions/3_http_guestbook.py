# Challenge 1:
# Get this working. Run this with Python, then figure out how to access the
# server and see the example website.
#
# Hint: Try going to http://localhost:8080/

# Challenge 2:
# Visit the contact page. Examine the terminal output every time you submit
# data on the contact page. Try typing different messages.
# Can you "extract" the name from the URL? Your goal for Challenge 2 is to have
# the server greet the user with their name on this page, in addition to the
# HTML contents.
#
# Hint: Try path.split('=') to split by the "equals" sign

# Challenge 3:
# Create a list called "guestbook". Append the name to this list every time
# they hit Submit.

# Challenge 4:
# Now, render the list on the page as a list of bullet points.

# Challenge 5:
# Can you connect to other student's servers?

# Advanced Bonus Challenge:
# Make a link "X" next to each guestbook item that, when clicked, will delete
# each individual guestbook item.

import socketserver
import socket

def index():
    return '''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/contact">Contact me</a> <br />
    '''

def about_me():
    return '''
        <h1>About me</h1>
        <p>My name is Ash Ketchum</p>
        <p>I have a Pikachu</p>
    '''
guestbook = []

def contact_me(path):
    print('---CONTACT ME')
    print(path)
    if '=' not in path:
        name = ''
    else:
        # Challenge 2
        other_crap, name = path.split('=')
        # name gets + signs instead of spaces, lets fix that
        name = name.replace('+', ' ')
        print(name)

        # Challenge 3
        guestbook.append(name)

    # Challenge 4
    guestbook_html = '\n<li>'.join(guestbook)
    print('---')
    return f'''
        <h1>Contact</h1>
        <h2>Hello {name}</h2>
        <ol>
            <li>{guestbook_html}
        </ol>
        <form method="GET" action="/contact">
            <input name="myname" placeholder="Your name" />
            <button>Submit</button>
        </form>
    '''

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Every time a request comes in, it calls this method

        ## Step 1, parse the request data
        # Get the top line of the request
        top_line = self.rfile.readline().decode('ascii')
        method, path, http_version = top_line.split(' ', 2)
        print('--> Receiving %s request for %s' % (method, path))

        # Get the HTML value associated with the path that is getting requested
        # from the pages dictionary
        if path == '/':
            body = index()
            self.wfile.write(b'HTTP/1.0 200 OK\n')
        elif path == '/about-me':
            body = about_me()
            self.wfile.write(b'HTTP/1.0 200 OK\n')
        elif path.startswith('/contact'):
            body = contact_me(path)
            self.wfile.write(b'HTTP/1.0 200 OK\n')
        else:
            # Couldn't find page, send back 404 error page, and be sure to set
            # the 404 status code in the header
            body = '<h1>Oh no, 404! Jigglypuff prolly stole it.</h1>'
            self.wfile.write(b'HTTP/1.0 404 Not Found\n')

        # Write the response headers text/html 
        self.wfile.write(b'Content-Type: text/html\n')

        # The HTTP standard mandates an extra return character here, separating
        # the headers from the body of the response.
        self.wfile.write(b'\n')
        self.wfile.write(bytes(body, 'ascii'))
        self.wfile.close()


if __name__ == "__main__":
    PORT = 8080
    server = None
    try:
        socketserver.TCPServer.allow_reuse_address = True
        server = socketserver.TCPServer(('', PORT), RequestHandler)
        print('--------> Starting server on port ', PORT)
        server.serve_forever()

    finally:
        print('\n-------> Shutting down the web server')
        if server:
            server.server_close()

