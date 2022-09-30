"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

# Why did line 26 give TypeError for list indices before converted into integers? and it fixed after int()


numbers.sort()

l = len(numbers)
if not( (l % 2) == 0):
   print(numbers[int(math.floor(l/2))])

else:
    print(l)
    print( (numbers[int(l/2) ] + numbers[int( (l/2)-1 ) ] )/2  )  
