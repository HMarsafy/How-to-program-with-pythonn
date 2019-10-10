def addition(x,y):
	return x+y
print(addition(5,3))

z=addition(10,5)
print(z)

print(addition("Hey"," There"))

# X & Y must be the same type.(numbers or string)
# addition(5 , "Hey")  : Generate an error(because not the same type)
y=addition(5.5 , 10)
print(y)