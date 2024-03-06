# [reduce] Write a Python function calculate_factorial that takes an integer as input and uses the reduce function 
# to return the factorial of that number.

from functools import reduce

def calculate_factorial(num: int):
    if num == 0:
        return 1
    else:
        return reduce(lambda x,y: x*y, range(1, num+1))

print(calculate_factorial(7))