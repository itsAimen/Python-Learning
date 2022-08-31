# When not operator is applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.
# We add the not operator to the very beginning of the statement.

# not 1 + 1 == 2   False
# not 7 < 0        True

Credits = 120
gpa = 1.8

if not Credits >= 120:
    print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate")
if not Credits >= 120 and gpa >= 2.0:
    print("You do not meet either requirements to graduate!")
