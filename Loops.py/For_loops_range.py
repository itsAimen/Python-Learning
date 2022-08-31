# if we wanted to print out a "Learning Loops!" message six times using a for loop, 
# we would follow this structure:

# promise = "I will finish the python loops module!"  

# for <temporary variable> in <list of length 6>:
#    print("Learning Loops!")

# To create arbitrary collections of any length, we can pair our for loops
# with the trusty Python built-in function range()

for promise in range(6):
    print("I will finish the python loops module!")

for name in range(11):
    name = "aimen"
    print(name)

for num in range(5):
    print(1,2,3,4)

for message in range(2, 10, 2):
    print("Hello World!")


# If we are curious about which loop iteration (step) we are on, we can use temp to track it.
# Since our range starts at 0, we will add + 1 to our temp to represent 
# how many iterations (steps) our loop takes more accurately

for promise in range(6):
    print("I will finish the python loops module!"
    + str(promise +1))

I_will = "I will finish the python loops module!"

for temp in range(5):
    print(I_will)