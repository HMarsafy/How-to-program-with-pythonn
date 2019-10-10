game = [[0,0,0],[0,0,0],[0,0,0]]
def game_board(game_map , player=0 , row=0 , coulmn = 0 , disply=False):
	try:
		print("   0  1  2")
		if not disply:
			game_map[row][coulmn]= player
		for count,row in enumerate(game_map):
			print(count,row)
		return game_map
	
	#except:   
		#print("There is something wrong !!!")
	except IndexError as e:  # this for index error only
		print("Error: make sure u input row/coulmn  as 0 , 1 or 2 ?" ,e)
		#(this fourmela bellow is general for any type of error)
	except Exception as e:
		print("something want very wrong !!!")
	#search on google for:
	  #else:
	  #finally:
#game = game_board(game , disply = True)
game = game_board(game_board , player = 1 , row = 3 , coulmn = 1)