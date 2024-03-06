# [map] Create a function convert_to_uppercase that takes a list of strings as input and uses the map 
# function to return a new list with all the strings converted to uppercase.

def convert_to_uppercase(string: str):
    return string.upper()

list_of_str = ['a','b', 'c', 'd', 'e']
print(list(map(convert_to_uppercase, list_of_str)))
