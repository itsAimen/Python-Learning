def calculator():

    print("Welcome, My name is Aimen. I'm your Calculator!")
    print("Let's start by having your first and last name.")
# Asks user to enter their first and last name
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("Select Operation")
# Shows user the following calculation options:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Please Enter the Operation of Choice: ")
# Asks user to enter their choice of calculation
    x = int(input("Please Enter the first number: "))
    y = int(input("Please Enter the second number: "))

    if choice == "1":
        print(x, "+", y, "=", (x+y))
    elif choice == "2":
        print(x, "-", y, "=", (x-y))
    elif choice == "3":
        print(x, "*", y, "=", (x*y))
    elif choice == "4":
        print(x, "/", y, "=", (x/y))
    else:
        print("Error")


calculator()
choice2 = input("Would you like to do another calculation? ")
if choice2 == "yes":
    calculator()
else:
    print("Have a good day.")
