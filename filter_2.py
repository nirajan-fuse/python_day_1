# [filter] Write a Python function filter_long_strings that takes a list of strings as input and uses the filter 
# function to return a new list containing strings with more than 5 characters.

def filter_long_strings(string: str):
    if len(string) > 5:
        return True
    else:
        return False
    
list_of_string = ['Nirajan', 'tree', 'Thakuri', 'hello']
print(list(filter(filter_long_strings, list_of_string)))