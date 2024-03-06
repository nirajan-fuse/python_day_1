# [*args] Write a Python function concat_strings that takes any numbers of strings as arguments and returns a single concatenated string.

def concatenation(*args):
    concat_strings = ''
    for string in args:
        if type(string) is not str:
            return 'string value only!'
        concat_strings += string
    
    return concat_strings

print(concatenation('a', 'b', 'c', 'd', 'e'))

print(concatenation('Nirajan', ' ', 'Thakuri'))

print(concatenation(1,2,3,4))

print(concatenation(True, False))