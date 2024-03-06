# [set comprehension] Given two strings, write a Python program to create a set using set comprehension that contains all 
# the characters that are common in both strings.

string_1 = "I am so blue I'm greener than purple."
string__2 = "I stepped on a Corn Flake, now I'm a Cereal Killer."

common_characters = {character for character in string_1 if character in string__2}

print(sorted(common_characters))