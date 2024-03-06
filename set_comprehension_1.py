# [set comprehension] Given a list of numbers, create a set using set comprehension that contains only unique even numbers.

list_of_nums = [1,2,3,4,5,6,7,8,9,8,5,6,3,4,7,8,2,3,7,8,2,9]

unique_even_number = {num for num in list_of_nums if num%2==0}

print(sorted(unique_even_number))

