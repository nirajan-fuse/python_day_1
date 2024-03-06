# [filter] Implement a function called filter_prime_numbers that takes a list of integers as input and uses the filter 
# function to return a new list containing only the prime numbers.

def filter_prime_numbers(num: int):
    if num==1:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True
    
list_of_int = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(filter_prime_numbers, list_of_int)))