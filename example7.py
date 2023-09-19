#!python3

"""
we can retrieve text from the www and store it into variables using request page
"""

import requests


x = requests.get("https://sd.deltasd.bc.ca")
print(x.text)

"""
This will retrieve the entire webpage!
"""