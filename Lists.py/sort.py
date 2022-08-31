# .sort() / sorted() is a method and a build-in function to a sort a list
# .sort() can sort lists numerically or alphabetically 

names = ["Munaya", "Aimen", "Harumi", "Zeel"]

names.sort()
print(names)
# We can also reverse from ascending order to decending order by:
names.sort(reverse=True)
print(names)

numbers = [5, 19, 2, 8, 0]
numbers.sort()
print(numbers)

# sorted() comes before the list as compared to .sort() which comes after the list
# sorted() creates a new list instead of modifying the one that already exists 

names = ["Munaya", "Aimen", "Harumi", "Zeel"]
sorted_names= sorted(names)
print(sorted_names)
print(names)

# note sorted() did not change the names variable 

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games_sorted)
print(games)
