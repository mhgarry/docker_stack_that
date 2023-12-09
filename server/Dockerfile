# import base image, the latest version of python from docker hub
FROM python:latest

# Importing server.py and index.html and adding them to /server directory
ADD server.py /server/
ADD index.html /server/

# Using workdir to set our root directory to /server
WORKDIR /server/