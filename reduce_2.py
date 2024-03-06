# [reduce] Implement a function called concatenate_strings that takes a list of strings as input 
# and uses the reduce function to return a single string containing the concatenation of all the elements.

from functools import reduce

def concatenate_string(string_1: str, string_2: str):
    return string_1+string_2


list_of_str = ['a', 'b', 'c', 'd', 'e']
print(reduce(concatenate_string, list_of_str))