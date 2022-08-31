number = int(input("Enter a number: "))
# It will ask the user to enter a number
calculation = number % 2 
# Modulos operator is used because:
# it will calculate if the number has a remainder of 0 if so, then the number is even
# else it is odd
if (calculation == 0):
# This will compare and check if the number is even or odd. 
    print("It is an even number")
else:
    print("It is an odd number")