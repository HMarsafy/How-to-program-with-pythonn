# go back to the 1st example in the tutorial_8
game = " I want play this game"
def my_function ():
	global game     #make " game " variable a "GLOBAL" variable.
	game=" this game"
	
print(game)
my_function()
print(game)
''' SO THE O/P WILL BE:
     I want play this game
     this game
    SO THIS IS A GLOBAL VARIABLE WHICH CAN BE ACCESSED ANYWHERE'''

