game = [[3,3,3],
		[3,3,3],
		[3,3,3]]  
		#enumerate fn: its a function that iterate on a list (for example) and returns its values and the order of the values.
print("   0  1  2")
for count,row in enumerate(game):
	print(count , row) # this print the entire row and its order.
	for item in row:  #this iterate on each element in the 2D List.
		print(item)
 	