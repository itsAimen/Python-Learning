# Two-dimensional lists can be accessed similar to their one-dimensional counterpart. Instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first

class_name_test = [["Jenny", 90], ["Alexus", 85.5],["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test [2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)