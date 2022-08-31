# Lets assume we have a list of letters:

letters = ["a", "b", "c", "d", "e", "f", "g"]

# Suppose we want to select from "b" through "f".
# We can do this using the following syntax: letters[start:end], where:
# start is the index of the first element that we want to include in our selection.
# In this case, we want to start at "b", which has index 1.
# end is the index of one more than the last index that we want to include
# The last element we want is "f", which has index 5, so end needs to be 6

sliced_list = letters[1:6]
print(sliced_list)

# note that the element at 6th index is not included

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

names = ["Aimen", "Ashar", "Hamza", "Ammar", "Haani"]
# if we want to slice the first 3 names first we would use:


print(names[:3])

# note that the element at 3rd index is not included

# if we want to slice the last 2 elements we would use negative index:


print(names[-2:])

# Notice that the colon is now at the end

# For all but the last element we would use


print(names[:-1])

# For all except for the last 3 we would use

print(names[:-3])

