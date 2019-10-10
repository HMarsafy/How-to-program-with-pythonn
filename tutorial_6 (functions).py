''' if you need a part of code many times in your code....
    make main function and call it whenever u want it '''

'''the problem is that i need this:
print("   a  b  c")
for count,row in enumerate(game):
	print(count , row)
everytime the player play 
so we need a fn.........  '''
# function defination.
def game_board():
	print("   0  1  2")
	for count,row in enumerate(game):
		print(count , row)
game =[[0,0,0],[0,0,0],[0,0,0]]
game_board()
game[0][2]=1
game_board()
game[2][1]=1
game_board()
x=game_board    #nice
game[1][1]=1
x()
