# lists can be added to each other using the plus symbol +. As shown in the code block, this will result in a new list containing the same items in the same order with the first list’s items coming first
# This will not work for adding one item at a time (use .append() method). In order to add one item, create a new list with a single value and then use the plus symbol to add the list

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

new_orders = ["lilac", "iris"]
orders_combined = orders + ["lilac", "iris"]
print(orders_combined)

family_of_3 = ["Dad", "Mom", "Son"]
new_addition = ["Baby Sister"]
family = family_of_3 + ["Baby Sister"]
print(family)