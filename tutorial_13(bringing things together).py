game=[[1,0,2],
      [1,2,0],
      [1,2,1]]
diags2=[]
diags = []
check=[]
def win(gametable):
	for row in gametable:
		print(row)
		flag=True
		for item in row:
			if (item != row[0]  or row[0] ==0):
				flag=False
		if flag:
			print(f"player {diags2[0]} is the winner horizontally (--) !")	

	i=0
	for row in gametable:
		print(row)
		flag=True
		for row in gametable:
			check.append(row[i])
		for item in check:
			if (item !=check[0]  or  check[0] ==0):
				flag=False	
		if flag:
			print(f"player {check[0]} is the winner vertically (|)!")	
		check.clear()
		i=i+1
	'''
	count function:
	          # it's a function that returns the number of repeated times of
	           of certain element in a list.
	           example:
	                # y=[1,2,1,3,1,4,1,5]
	                y.count(1)--->4
	                (it means that 1 is repeated 4 times in the list)
	'''
	for cols , rows in enumerate(reversed(range(len(game)))):
		diags2.append(game[cols][rows])
	if diags2.count(diags2[0])==len(diags2) and diags2[0]!=0:
		print(f"player {diags2[0]} is the winner diagnaly(/) !")	

	for x in range(len(game)):       
		diags.append(game[x][x])
	if diags.count(diags[0])==len(diags) and diags[0]!=0:
		print(f"player {diags[0]} is the winner diagnaly(\) !")

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
play=True
players=[1,2]
while play:
	game=[[0,0,0],
	      [0,0,0],
	      [0,0,0]]
	game_won=False #means that the game hasn't finished yet.
	game = game_board(game , disply = True)
	while not game_won:
		'''
		input function returns "string" so w must make it "integar"
		'''
		current_player=1
		coulmn_choice=int(input("what coulmn do you want to play?  (0,1,2) :"))
		row_choice=int(input("what row do you want to play?  (0,1,2) :"))
		game = game_board(game , current_player  , row_choice , coulmn_choice )







#game = game_board(game , disply = True)
#game = game_board(game_board , player = 1 , row = 3 , coulmn = 1)

