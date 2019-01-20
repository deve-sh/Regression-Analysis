# Program to find out the covariance between the two numbers.

def cov(x,y):	# x,y -> lists
	if( len(x) != len(y) ):
		return 0	# Error
	else:
		n = len(x)

		# Means of both the lists.

		meanx = sum(x)/n
		meany = sum(y)/n
		
		# Cummulative Sum

		cumsum = 0

		# Zip of both the list to contain both the quantities.

		z = list(zip(x,y))

		for i in z :
			cumsum += (i[0]-meanx)*(i[1]-meany)
		
		return (cumsum / n)