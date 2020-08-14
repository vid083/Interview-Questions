"""
There’s a classic coding interview question named FizzBuzz that can be solved by iterating over both indices and values. In FizzBuzz, you are given a list of integers. Your task is to do the following:

Replace all integers that are evenly divisible by 3 with "fizz"
Replace all integers divisible by 5 with "buzz"
Replace all integers divisible by both 3 and 5 with "fizzbuzz"
"""

numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
     if num % 3 == 0 and num % 5 == 0:
         numbers[i] = 'fizzbuzz'
     elif num % 3 == 0:
         numbers[i] = 'fizz'
     elif num % 5 == 0:
         numbers[i] = 'buzz'

#output numbers:
#['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']