# Challenge 1:
# Get this working. Run this with Python, then figure out how to access the
# server and see "Hello Server World!"
#
# Hint: Try going to http://localhost:8080/

# Challenge 2:
# Examine the terminal output every time you visit the page. Experiment by
# typing in different addresses in the address bar of your browser and hitting
# enter. See what different output appears in the terminal.
#
# Once you have established a pattern, write pseudocode for an application that
# will show one message at localhost:8080 followed by "/" , another at
# "/about-me", and yet another at "/contact-me".
# Psuedocode:
# Get the path of the request
# if path of request is /about-me, respond accordingly
#
# Bonus Challenge:
# Implement the Python code based on the pseudocode above and confirm it is
# working.
#
#

import socketserver

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Every time a request comes in, it calls this method

        # The request data is in a file-like object called 'self.rfile' that we
        # can read. We need to "decode" it since it comes in as bytes.
        print('---- REQUEST -------------')
        request = self.rfile.readline().decode('ascii').strip()

        print(request)
        # First splits the string after GET, then splits again to get the value before HTTP/1.1
        path = request.split('GET',1)[1].split()[0]
        print(path)
        if path == '/about-me':
            self.wfile.write(b'Welcome, this is the about me page')
            self.wfile.close()
        elif path == '/contact-me':
            self.wfile.write(b'Please don\'t contact me')
            self.wfile.close()
        elif path == '/':
            self.wfile.write(b'Hello Server World!')
            self.wfile.close()

        print('--------------------------')

        # Just say the same thing to all requests



if __name__ == "__main__":
    PORT = 8096
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
