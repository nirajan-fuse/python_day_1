# [list comprehension] Given a list of strings, create a new list that contains only the strings with more than 5 characters 
# using list comprehension.

list_of_strings = ['thakuri', 'hello', 'hi', 'wonderful']

new_list = [string for string in list_of_strings if len(string) > 5]

print(new_list)