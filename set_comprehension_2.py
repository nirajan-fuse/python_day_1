# [set comprehension] Given a list of words, write a Python program to create a set using set comprehension that contains all 
# the unique characters present in the words.

list_of_words = ['fusemachines', 'f1soft', 'leapfrog', 'verisk', 'deerwalk']

unique_characters = {character for word in list_of_words for character in word}

print(sorted(unique_characters))