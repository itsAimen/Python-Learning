# A-built-in Python function to create a sequence of integers
# range() creates a list of numbers
# it stops one number behind the input given, i.e input(10) would stop at 9. 
# executing " input(10) " would give us the output of " (1, 10) " however,
# to list the numbers from 0-9 we need to use " list " command

my_range = range(10)
print(my_range)
print(list(my_range))

number_list = range(3)
print(list(number_list))

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# by default range() starts with 0 however,
# using two inputs it can start with the first number provided 

start_with_2 = range(2,11)
print(list(start_with_2))

# if we use a third input it gives us an oppurnity to skip numbers 

skip = range(2, 4, 2)
print(list(skip))

skips_in_2 = range(2, 8, 2)
print(list(skips_in_2))

skips_in_5 = range(10, 50, 5)
print(list(skips_in_5))

skips_in_20 = range(2, 90, 20)
print(list(skips_in_20))

# to skip using 3 indix method:
# the 1st index degit tells the computer to start at the number given
# the 2nd index degit tells the computer to stop one degit before the number given
# the 3rd index digit tells the computer to skip by these many degits in between

test = range(5, 44, 2)
print(list(test))

test1 = range(10, 65, 2)
print(list(test1))