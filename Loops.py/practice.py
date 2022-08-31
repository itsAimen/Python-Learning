# Adding two lists together using for loops

#first way

list_1 = ["Shirt", "Pants", "Sweater", "Socks", "Jacket"] 
list_2 = ["Hat", "Watch", "Shoes"]
for list_3 in list_1:
    list_3 = list_1 + list_2
print(list_3)
#second way
list_1 = ["Shirt", "Pants", "Sweater", "Socks", "Jacket"]
list_2 = ["Hat", "Watch", "Shoes"]
for list_3 in list_2:
    list_1.append(list_3)
print(list_1)

#sum = 5
#numbers = [1,10,2]
#for sum in numbers:
#print(sum +1)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_5 = []

length = len(list_1)
for i in range(length):
    result = list_1[i] + list_2[i]
    print(list_1[i], "+" ,list_2[i], "=", result)
    list_5.append(result)
print(list_5)