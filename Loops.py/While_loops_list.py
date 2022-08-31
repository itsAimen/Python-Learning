# while loop will repeatedly execute a code block as long as a condition evaluates to 'True'
# The condition of a while loop is always checked first before the block of code runs
# If the condition is not met initially, then the code block will not run 

# We are going to write a while loop to iterate over the provided list python_topics
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# First, we will need a variable to represent the length of the list. 
# This will help us know how many times our while loop needs to iterate.
length = len(python_topics)

#Next, we will require a variable to compare to our length variable to make sure 
# we are able to implement a condition that eventually allows the loop to stop
index = 0

while index < length:
# on each iteration print "I am learning about <element from python_topics>"
    print("I am learning about")    
# We want our loop to iterate over the list of python_topics
    print(python_topics[index])
    index += 1