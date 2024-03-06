# [dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase 
# alphabets (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.

list_of_alphabets = ['a', 'B', 'c', 'd', 'E']

ASCII_corresponding_dict = {alphabet.lower():ord(alphabet.lower()) for alphabet in list_of_alphabets}

print(ASCII_corresponding_dict)