#!Python3
'''
Take a look at https://www.w3schools.com/python/python_ref_string.asp
Strings have special functions called methods that operate 
Methods are used by including them after the variable
'''

x = "This is a string"

x.lower()
print(x)
'''
Note that the method does not alter the original string. However, we can store the output of the method by assigning it to a variable
'''

y = x.lower()
print(f"Note the lower case version is: {y}")


