# Make a Python script that prints out the version of the requests library.
import requests

print(requests.__version__)

# Modify your Python script to GET the Google homepage.
output = requests.get("https://www.google.com/")

# Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub.
from os import getcwd

raw_file = requests.get("https://raw.githubusercontent.com/GraceFu/CMPUT404-Lab1/master/lab1.py")
filename = getcwd() + "lab1.txt"
f = open(filename,'w')
f.write(raw_file.text)