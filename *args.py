#What does the *args do in Python?

#  *args is used as a parameter in the function header. It gives the ability to pass N (variable) number of arguments.

# Python code to demonstrate 
# *args for dynamic arguments 
def fn(*argList):  
    for argx in argList:  
        print (argx) 
    
fn('I', 'am', 'Learning', 'Python')

""" 
output:
I
am
Learning
Python
"""
 