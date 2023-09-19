#!python3

"""
example of string.split

You may want to explore other string methods

https://www.w3schools.com/python/python_ref_string.asp
"""


myString = "My dog has fleas. My cat does not."

list1 = myString.split(" ")
print("Separating by spaces gives list:" , list1)

list2 = myString.split(".")
print("Separating by . gives list", list2)

