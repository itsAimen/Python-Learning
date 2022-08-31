last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = [["physics"], ["calculus"], ["poetry"], ["history"]]
grades = [["98"], ["97"], ["85"],["88"]]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
computer_science = ["computer science", 100]
gradebook.append(computer_science)
print(computer_science)
visual_arts = ["visual arts", 93]
gradebook.append(visual_arts)
print(visual_arts)
# add extra 5 points to visual arts 
gradebook[-1][-1] = 98
print(gradebook)
# remove grades from poetry
gradebook[2].remove(85)
print(gradebook)
# add pass to poetry
gradebook[2].append("Pass")
print(gradebook)
# combine old semester and new semester grades
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)