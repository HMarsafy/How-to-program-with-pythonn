# last time we modified the variable " game " inside the function.
#but if we try this
game = " I want play this game"
print(id(game))
def my_function ():
	game=" this game"
	print(game)
	print(id(game))
print(game)
my_function()
print(game)
print(id(game))
#as we see there is no change.and we can't modify the " game " variable.
# and we can't access the " game " variable inside the fn too.
# but after we declared a new " game " variable inside the fn,we accessed it.
# WHY ?
   #because string is mutable.
 # the "game" variable's ID of the fn is diffrent from the outside "game" varaible.
 # go to part 2.