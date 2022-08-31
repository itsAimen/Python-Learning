# operator or combines two expressions into a larger expression that is True if either component is True

# Consider the statement

# "Oranges are a fruit or apples are a vegetable."
# This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True

bouquet_iris = 13
bouquet_jasmine = 19

if bouquet_iris >= 6 or bouquet_jasmine <= 24:
    print("What a beautiful bouquet!")

# This will appear as True because one of the statement is True

if bouquet_iris >= 13 or bouquet_jasmine < 19: 
    print("What a beautiful bouquet!")

# This will appear as False because both statements are False

if bouquet_iris >= 15 or bouquet_jasmine < 19: 
    print("What a beautiful bouquet!")