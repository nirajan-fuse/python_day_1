# [*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. Test your function with various input cases.

def addition(*args):
    sum = 0
    for num in args:
        if type(num) is not int:
            return 'Numeric value only!'
        sum += num
    
    return sum

print(addition(2,3,4,5))

print(addition(23,54,-23,0,2))

print(addition('a','b','c'))

print(addition(True, False))