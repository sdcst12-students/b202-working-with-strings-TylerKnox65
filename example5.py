#!python3

"""
Read through the file at https://www.w3schools.com/python/python_strings.asp
We want to pay particular attention to the fact that strings are actually like lists and we can access individual characters in a string as elements
Use a breakpoint on line 9 and step through this program
"""

x = "This is a string"
'''
access individual characters at a position starting at 0
'''
print(x, x[0])
print(x, x[1])

'''
access multiple characters starting at a position and ending just before a position
'''
print(x, x[2:6] )

'''
if you skip either the beginning or the ending, it will start at the beginning or the ending
'''
print(x, x[:6])
print(x, x[6:])

'''
Note you can also count from the end using negative indexes
'''
print(x, x[-3:])
print(x, x[-6:-4])