from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Only first test server!')


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

# from http.server import BaseHTTPRequestHandler
# from http.server import HTTPServer

# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#   server_address = ('', 8000)
#   httpd = server_class(server_address, handler_class)
#   try:
#       httpd.serve_forever()
#   except KeyboardInterrupt:
#       httpd.server_close()