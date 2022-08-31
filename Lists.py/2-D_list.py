# Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
print(heights)
ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages)

names = [["Sarim", "Dumb"], ["Aimen", "Smart"], ["Ashar", "Sweet"]]
#names = ["Sarim"=0, "Dumb"=1]=0, ["Aimen",=0 "Smart"=1]=1, ["Ashar=0", "Sweet=1"]=2
#aimens = names[0]-----> this index is overall index of the bracket 
#aimens = names[0][0]----->first index will be the overall index and 
#second index will be the index of bracket

sarimkanam = names[0][0]
aimenkanam = names[1][0]

print(sarimkanam +" "+ aimenkanam)