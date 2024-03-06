# [dictionary comprehension] Given two lists one containing keys and another containing values, create a dictionary using 
# dictionary comprehension.

key_list = ['Apple', 'Banana', 'Cat', 'Door', 'Elephant']

value_list = [3, 6, 1, 2, 0]

comprehended_dict = {k:v for k, v in zip(key_list, value_list)}

print(comprehended_dict)