"""
What does the **kwargs do in Python?

**kwargs syntax can be used in a Python function declaration.let's pass N (variable) number of arguments which can be named or keyworded.

Python code to demonstrate **kwargs for dynamic + named arguments 
"""
def fn(**kwargs):  
    for emp, age in kwargs.items(): 
        print ("%s's age is %s." %(emp, age)) 
    
fn(John=25, Kalley=22, Tom=32)

"""
output:
John's age is 25.
Kalley's age is 22.
Tom's age is 32.
"""