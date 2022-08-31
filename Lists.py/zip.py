# The zip() function allows us to quickly combine associated data-sets 
# without needing to rely on multi-dimensional lists

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

# If we wanted to create a nested list that paired each name with a height,
# we could use the built-in function zip()
# The zip() function takes two (or more) lists as inputs and 
# returns an object that contains a list of pairs.

names_and_heights = zip(names, heights)
example = list(names_and_heights)
print(example)

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)