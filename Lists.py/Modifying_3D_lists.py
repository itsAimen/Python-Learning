# To change a value in a two-dimensional list, reassign the value using the specific index
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak","Medium", False]]
print(customer_data)
customer_data[2][2] = False 
customer_data[1].remove(False)
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)