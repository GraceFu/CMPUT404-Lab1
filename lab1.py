# Make a Python script that prints out the version of the requests library.
import requests

print(requests.__version__)

# Modify your Python script to GET the Google homepage.
output = requests.get("https://www.baidu.com/")
