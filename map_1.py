# [map] Write a Python function square_numbers that takes a list of integers as input and uses the map function 
# to return a new list containing the square of each element.

def square_numbers(num: int):
    return num ** 2

list_of_int = [1,2,3,4,5]

print(list(map(square_numbers, list_of_int)))