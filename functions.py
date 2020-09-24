"""A function is a subprogram that acts on data and often returns a value. A function is used in order to avoid the repetition of certiain blocks of code.

For E.g. input() is a function which allows the user to give input and len() is a function wich returns the lenght of a string"""

"""
Functions are mainly of two types:
1. 'Built in Functions': These are the functions which come pre-installed with python interpreter, for eg., input() These can be identified as all functions have "()"

2. 'Functions in a module': These are functions which can be used if a particular module/library of python is imported. For E.g., randint() is a function is the random library. These can be identified as all functions for modules are written as 'moduleName.functionName()'. E.g. random.randint()

3. 'User Defined Functions': These are the functions which are created by the user inorder to solve a particular problem or to avoid the repition of a certain block of code
"""

#Defining a Function 
"""We will here define a function and name it 'name' to return "Hello World" whenever called."""

def name():
  print("Hello World")
  return
#Here def is short for 'Define Function'
#You can name the function anything


#Calling a function:
"""We Will now call the function in our program. For this purpose all we need to do is write the name of the function with its parameters as the arguments (more on that ahead)"""
name()
