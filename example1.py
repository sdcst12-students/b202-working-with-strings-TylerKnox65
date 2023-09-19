#!python

'''
Using the __name__ variable
Sometimes you may want to reuse code.  You can use functions or objects that are defined in other files and import them into your current file.

Suppose we want to import functions from a file called ext1.py
We can import the ext1 file and call functions that are in that file.  Note that we need to specify that the files are not located in our current file, and that they exist in the imported file.
See lines 13 and 14
Note however, that when we import the file, it runs any commands that are in the main block of code.  We might not want any of those to run. Now change line 13 so that it imports ext2 instead.  You should notice that although ext1.py and ext2.py are very similar files, one uses a conditional check to see if the file is the main file, or if it's being imported into the main file.  If you ran each program on their own, they would behave the same way.
It is a good idea to start structuring all of your code this way, as you never know when you will want to import your code into other files.  This is also how external file assertions and tests can be done to mark your assignments.
'''
import ext1
ext1.f1()
