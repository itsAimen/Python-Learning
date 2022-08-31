# A TypeError is reported by the Python interpreter when an operation is applied to a variable of an inappropriate type
# This can occur when one attempts to use an operator on something of the incorrect type
# Some common type errors are:
# Accidentally adding or subtracting a string value.
# Call a function on something of the incorrect type. 

length = 2
width = 12
area = length * width

# print("The rectangle area is" + area )
# This would give a type error because instead of using "," we misplaced a "+" instead.

print("The rectangle area is" , area) 