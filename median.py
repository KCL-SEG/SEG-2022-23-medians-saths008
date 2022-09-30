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


numbers.sort()
print(numbers)
l = len(numbers)
print(l)
if not( (l % 2) == 0):
   print(numbers[int(floor(l/2))])
   print(l)
else:
    print(l)
    print( (numbers[int(l/2) ] + numbers[int( (l/2)-1 ) ] )/2  )  
