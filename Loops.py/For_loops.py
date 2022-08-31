# a for loop, a type of definite iteration.
# In a for loop, we will know in advance how many times the loop will need to iterate 
# because we will be working on a collection with a predefined length.
# The general structure of a for loop is
# for <temporary variable> in <collection>:
#  <action> 
# 1. A for keyword indicates the start of a for loop.
# 2. A <temporary variable> that is used to represent 
# the value of the element in the collection the loop is currently on.
# 3. An in keyword separates the temporary variable from the collection used for iteration
# 4. A <collection> to loop over. In our examples, we will be using a list
# 5. An <action> to do anything on each iteration of the loop.

import numbers


ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:
    print(ingredient)

# ingredient is the <temporary variable>.
# ingredients is our <collection>.
# print(ingredient) was the <action> performed on every iteration using 
# the temporary variable of ingredient.

loops = ["this", "is", "so", "much", "faster", "now"]
for message in loops:
    print(message)

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)
for sport in sport_games:
    print(sport)

flowers = ["Roses", "Jasmine", "Orchid", "Marigold", "Iris", "Lilac"]
for flower in flowers:
    print(flower)

eating_routine = ["Breakfast", "Snack", "Lunch", "Snack", "Dinner"]
for meals in eating_routine:
    print(meals)

numbers = [4, 6 ,7, 8, 9, 0, 16, 18, 20, 40, 55]
for number in numbers:
    print(number)