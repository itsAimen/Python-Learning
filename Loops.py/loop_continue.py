# The continue keyword is used inside a loop to skip the remaining code,
# inside a loop to skip the remaining code inside the loop code bloack and begin 
# the next loop interation 

# Similar to when we were using the break control statement, our continue control statement 
# is usually paired with some form of a conditional (if/elif/else)

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i <= 0:
        continue
    print(i)

# When our loop first encountered an element (-1) that met the conditions of the if statement,
# it checked the code inside the block and saw the continue. When the loop then encounters
# a continue statement it immediately skips the current iteration and moves onto the next
# element in the list (4)

# The output of the list only printed positive integers in the list because every time our loop
# entered the if statement and saw the continue statement it simply moved to 
# the next iteration of the list and thus never reached the print statement.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for entry in ages:
    if entry < 21:
        continue
    print(entry)