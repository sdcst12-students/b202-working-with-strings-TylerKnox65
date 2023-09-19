#!python3

from var1 import x

'''
Note that we can import the variable x from the var1.py file. We do need to make sure that we use the special variable __name__ to prevent the print statement from running
'''

print("=")
print("")
print(f"The value of x that we retrieved from var1 was \"{x}\"")
print("")
print("=")
