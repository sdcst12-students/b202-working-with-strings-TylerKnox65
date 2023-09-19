#!python3

'''
importing files into your current namespace

We are going to import a function from a file called imp1.py
Notice that the import format is a little bit different, however, by importing specific functions, we can avoid having to specify the file that they come from
You can use the * to import all functions and variables, or use specific names
Note that lines 19 and 20 are flagged as having errors because the names are not recognized.  When we imported from imp2, we only imported the triple function and not the more function.
'''

from imp1 import *
from imp2 import triple

x = double(3)
print(x)
y = triple(4)
print(y)
z = more()
z = imp2.more()