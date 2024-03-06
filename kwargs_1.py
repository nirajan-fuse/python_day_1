# [**kwargs] Write a Python function calculate_total_cost that calculates the total cost of items purchased from a store. 
# The function should accept multiple keyword arguments, where the key is the item name, and the value is the item's price. 
# The function should return the total cost of all items.

def calculate_total_cost(**kwargs):
    total_cost = 0

    for item, cost in kwargs.items():
        total_cost += cost

    return total_cost


list_of_item = {'Soap': 50, 'Brush': 70, 'Chicken': 350, 'Masala': 100}
print(calculate_total_cost(**list_of_item))


print(calculate_total_cost(Screwdriver=120, Pendrive=500, Cable=350))
