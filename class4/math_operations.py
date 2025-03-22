def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

import math_operations

print(math_operations.add(5, 3))      
print(math_operations.subtract(10, 4)) 

from math_operations import add

print(add(2, 7))  
