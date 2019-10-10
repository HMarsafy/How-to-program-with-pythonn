# but if we run this example.
game = [1,2,3,4,5,6]
def game_board(player =0 , row=0 , column=0 , disply=False):
	game = "a game"
	print(game)
game_board()
print(game)
''' the output will be
a game
[1, 2, 3, 4, 5, 6]
so we cant change the variable "game" outside the function.'''
#but if we make this:
game = [1,2,3,4,5,6]
def game_board(player =0 , row=0 , column=0 , disply=False):
	game[1] = 100
	print(game)
game_board()
print(game)
'''the output  will be:
[1, 100, 3, 4, 5, 6]
[1, 100, 3, 4, 5, 6]
so the variable inside and outside the fn are the same.
------->|| because w can change the value of the object but we cant
           change the object itself.
'''
'''AND TO SOLVE THIS PROBLEM WE WILL MAKE THE "game" VARIABLE A "" GLOBAL "" VARAIBLE '''
#GO TO PART 3.
