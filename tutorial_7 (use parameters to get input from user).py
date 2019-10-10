def game_board(player=0 , row=0 , coulmn=0 , disply=False): #u can intialize any parameter to any value.
	if not disply:
		game[row][coulmn]=player;                
	print("  0  1  2")                       
	for count,row in enumerate(game):
		print(count , row)
game =[[0,0,0],[0,0,0],[0,0,0]]

game_board(disply=True)
game_board(1,1,0) #or :game_board(player=1 , row=2 , coulmn = 1).
                  #or :game_board(1, row=2 , coulmn = 1). and so on....