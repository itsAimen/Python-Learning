#.count()
# Is a method to count the number of occurrences of an element in a list

list1 = ["Apple", "Apple", "Kiwi", "Banana", "Apple", "Kiwi", "Apple"]

apple_count = list1.count("Apple")
print(apple_count)

kiwi_count = list1.count("Kiwi")
print(kiwi_count)

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake",
    "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie",
    "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)