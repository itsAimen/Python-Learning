# a while loop is a form of indefinite iteration
# A while loop performs a set of instructions as long as a given condition is true
# The structure follow this pattern:
# while <conditional statement>:
#  <action>

count = 0
while count <= 3:
    # Loop Body
    print(count)
    count += 1

# 1. count is initially defined with the value of 0. 
# The conditional statement in the while loop is count <= 3, 
# which is true at the initial iteration of the loop, so the loop body executes

# 2. When the first iteration of the loop has finished, Python returns to the top of the loop 
# and checks the conditional again. 
# After the first iteration, count would be equal to 1 
# so the conditional still evaluates to True and so the loop continues

# 3. This continues until the count variable becomes 4. At that point, 
# when the conditional is tested it will no longer be True and the loop will stop

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")
