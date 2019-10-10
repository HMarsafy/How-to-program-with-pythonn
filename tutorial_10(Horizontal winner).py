game = [[1,1,1],
        [2,0,2],
        [0,0,0]]
def win(current_game):
	for row in current_game:
		print(row)
		flag=True
		for item in row:
			if (item != row[0]  or row[0] ==0):
				flag=False
		if flag:
			print("YOU ARE WINNER !")


win(game)