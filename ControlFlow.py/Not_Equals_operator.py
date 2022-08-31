# Not equal != is used to compare two values, variables or expressions to determine if they are NOT the same.
# If they are NOT the same, the operator returns 'True'. If they are the same, then it returns 'False'
# The operator takes the data type into account when making the comparion so a value of 10 would NOT be equal to the string value of "10" and the operator would return 'True' 
# If expressions are used, then they are evaluated to a value of 'True' or 'False' before comparison is made by the operator

calculation1 = 2 ** 4 != 6
calculation2 = 6 + 8 != 2 * 7
calculation3 = 6 ** 3 != 14

print(calculation1)
print(calculation2)
print(calculation3)