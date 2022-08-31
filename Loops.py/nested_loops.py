# loops can be nested inside other loops. Nested loops can be used to access items of lists 
# which are inside other lists. The item selected from the outer loop can be used as 
# the list for the inner loop to iterate over. 

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# To print each individual student
# We would actually need to nest our loops to be able loop through each sub-list

# Loop through each sublist
for team in project_teams:
# Loop elements in each sublist
    for student in team:
        print(student)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
# Loop through the sales_data list 
    print(location)
    for  element in location:
# Within our sales_data loop, nest a secondary loop to go through 
# each location sublist element and add the element value to scoops_sold
        scoops_sold += element
print(scoops_sold) # printed outside of the nested loop