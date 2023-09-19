"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""
import requests
x = requests.get("https://sd.deltasd.bc.ca")
print(x.text)