"""Given a binary string S. 
The task is to count the number of substrings that start and end with 1. 
For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.  
Input:
N = 4
S = 1111
Output: 6
Explanation: There are 6 substrings from
the given string. They are 11, 11, 11,
111, 111, 1111.  """

#PYTHON 3 CODE:

''' Function to return total number of binary
    substrings in the given string.
    n: Length of string
    s: Given string
'''

def binarySubstring(n,s):
    number_of_ones=s.count('1')
    return ((number_of_ones*(number_of_ones-1))//2)
