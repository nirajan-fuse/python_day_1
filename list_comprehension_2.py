# [list comprehension] Given two lists of integers, create a list that contains the product of each element of the first list 
# with the corresponding element in the second list using list comprehension.

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,9]

new_list = [n1*n2 for n1, n2 in zip(list_1, list_2)]

print(new_list)