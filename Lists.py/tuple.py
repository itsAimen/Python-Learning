# tuples are similar to lists however, once created they can not be edited 

user = ("Aimen", 21, "Painting")
print(user)
print(user[0])
print(user[1])
print(user[-1])
# if we try to edit the tuple:
# user.pop()
# it will give us an error because it can not change the original tuple 

# We can unpack a tuple by:
name, age, hobby = user 

print(name)
print(age)
print(hobby)

# One element tuple
one_element_tuple = (5)
print(one_element_tuple)
one_element_tuple_sp = (5,)
print(one_element_tuple_sp)