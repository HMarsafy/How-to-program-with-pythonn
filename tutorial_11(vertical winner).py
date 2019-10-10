game=[[1,2,0],
      [1,2,0],
      [1,2,0]]        #EXPLANING BELLOW
check=[]
def win(gametable):
	i=0
	for row in gametable:
		flag=True
		for row in gametable:
			check.append(row[i])
		for item in check:
			if (item !=check[0]  or  check[0] ==0):
				flag=False	
		if flag:
			print("Winner !")
		check.clear()
		i=i+1		
win(game)
""" save the first element in each row in a list called "check"
    then compare each element of this list:
    # if they are all equal unless the are equal zero :  print winner.
    # if they are all not equal or are equal but equal to zero : GO out.
    """
