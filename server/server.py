#!/usr/bin/env python3

# import server library
import http.server
import socketserver

#  initialize handler to manage requests from client
handler = http.server.SimpleHTTPRequestHandler
# initialize server with port 1234 using handler for requests 
with socketserver.TCPServer(("", 1234), handler) as httpd:
  # This instruction will keep the server running, waiting for requests from the client.
  httpd.serve_forever()