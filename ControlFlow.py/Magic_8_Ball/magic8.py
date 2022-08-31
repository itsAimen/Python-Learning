# The Magic 8-Ball is a popular toy developted that can answer any “Yes” or “No” question with a different fortune each time it executes

import random # To use the random function we need to import module at the top of the code

name = "Aimen"
question = "Am I a good league player?"
answer = ""
random_number = random.randint(1,9) # we can use the .randint() function from the random module to generate a random number from a range
print(random_number)

if random_number == 1:
    print("Yes - definitely.")
elif random_number == 2:
    print("It is decidedly so.")
elif random_number == 3:
    print("Without a doubt.")
elif random_number == 4:
    print("Reply hazy, try again.")
elif random_number == 5:
    print("Ask again later.")
elif random_number == 6:
    print("Better not tell you now.")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good.")
elif random_number == 9:
    print("Very doubtful.")
else: 
    answer = "Error"

print(name + " asks: " + question)