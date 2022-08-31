# A list method to remove an element from a specific index or a from the end of a list 
# Using .pop() without an index will remove whatever the last element of the list is
# If we wanted to know what element was deleted
# simply assign a variable to the call of the .pop() method.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# remove "Python 3"
data_science_topics.pop()
print(data_science_topics)
# remove "Algorithms"
data_science_topics.pop(3)
print(data_science_topics)

Pizza = ["Crust", "Sauce", "Cheese", "Onions", "Olives", "Mushrooms", "Green Pepper"]
Pizza.pop()
Pizza.pop(4)
print(Pizza)
