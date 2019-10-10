game =[[2,0,2],
       [1,2,0],
       [2,2,1]]

'''
static solution:
if game[0][0] == [1][1] == [2][2]:
	print("winner")
if game[0][2] == [1][1] == [2][0]:
	print("winner")
THIS IS WORKING BUT IT'S NOT DYNAMIC.
len(game) ---> 3
important note:
       #range(5):0,1,2,3,4
       #range(-2,2):-2,-1,0,1
       #in this ex:range(len(game)):0,1,2
important note:
       #reversed(range(3))---> 2 , 1 , 0 (inverted)
'''
diags = []
for ix in range(len(game)):       
	diags.append(game[ix][ix])
print(diags) 
# this way helps to take the left diagonal.
#to take the right diagonal :
game2= [[2,0,2],
        [1,2,0],
        [2,2,1]]
diags2=[]
'''
ZIP FUNCTION:
x=range(3)
y=[2,1,0]
for i in zip(x,y):
	print(i)
output---->(0,2)
           (1,1)
           (2,0)
z=[5,6,7]
for x in zip(x,y,z):
	print(x)
output---->(0,2,5)
           (1,1,6)
           (2,0,7)

'''
cols= list(reversed(range(len(game2))))  #list contain :[2 , 1 , 0]
rows = range(len(game2))                 #list contain :[0 , 1 , 2]
#for idx in rows:
#	print(idx,cols[idx])   to check that its hold the values upwards.
for cols , rows in zip(cols , rows):
	print(cols  , rows)
'''
output---->2 0
           1 1
           0 2
so |
   |
   V
   we can access the right diagonal
  OR
'''
for cols , rows in enumerate(reversed(range(len(game2)))):
	print(cols,rows)
	diags2.append(game2[cols][rows])
print(diags2)
#Well done
'''
so diags contain the left diagonal
and diags2 contain the right diagonal
'''


