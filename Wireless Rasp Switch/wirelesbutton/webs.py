#!/usr/bin/env python3
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
# Make sure the server is created at current directory
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']
os.chdir('./public')
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 9000), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()