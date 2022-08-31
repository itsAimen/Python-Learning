# negative indices can be used to reference elements in relation to the end of a list. This can be used to access single list elements or as part of defining a list range. For instance:

# To select the last element, my_list[-1].
# To select the last three elements, my_list[-3:].
# To select everything except the last two elements, my_list[:-2].

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[-1] # select the element with index 5 and save it to the variable
print(index5_element + last_element)
