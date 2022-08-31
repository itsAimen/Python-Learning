# List comprehensions provide a concise way for creating list. It consists of brackets 
# containing an expression followed by a for clause, then zero or more for if clauses:
# [Expression for Item in List <if Conditional>]
# The expressions can be anything - any kind of object can go into a list
# A comprehension always returns a list

# new_list = [<expression> for <element> in <collection>]
# 1. Takes an element in the list numbers
# 2. Assigns that element to a variable called num (our <element>)
# 3. Applies the <expression> on the element stored in num and adds the result 
#    to a new list called doubled
# 4. Repeats steps 1-3 for every other element in the numbers list (our <collection>)

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

