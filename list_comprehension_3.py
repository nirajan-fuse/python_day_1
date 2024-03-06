# [list comprehension] Given three lists list1, list2, and list3, each containing integers, write a Python program using list 
# comprehension to generate a new list of unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, 
# such that x + y + z = 0.

list_1 = [1,3,5,7,9,11,13,15]
list_2 = [-4, -5, -3, -7, -6, -2, -15]
list_3 = [-2, 2, 4, 0, -3, -6, 2]

new_list = [(x, y, z) for x, y, z in zip(list_1, list_2, list_3) if x+y+z==0]

print(new_list)