#!/usr/bin/env python3

# import urlib library to serve files from the server
import urllib.request

# set the url of the server and open the connection with the server on port 1234
url = urllib.request.urlopen("http://localhost:1234")

content = url.read()
# parse the server response 
parsedContent = content.decode("utf-8")

# print server response
print(parsedContent)

# close connection to server
url.close()