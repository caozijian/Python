
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8081
# if you got
# OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
# try to change your web server port number
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

