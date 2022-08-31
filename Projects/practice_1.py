grades = [52, 71, 83, 91, 22, 50]
print(grades)
print(grades[-1])
length = len(grades)

print(length)
print(grades[-2])

# flower = "orchid"
# print(flower[0])
# length = len(flower)
# print(length)

for grade in grades:
    if grade >= 90:
        print("You passed!")
        break
    print(grade)

food = ["Burger", "Rice", "Pizza"]
sauce = ["Ketchup", "Chutney", "Ranch"]

for i in range(3):
    print(food[i] + " with " + sauce[i])

number1 = [1,2,3]
number2 = [1,2,3]
# length1 = len(number1)
# length2 = len(number2)
# print(length1)
# print(length2)
for i in range(3):
    print(number1[i]) + (number2[i])