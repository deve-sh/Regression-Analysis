# Program for Standard Deviation and mean.

# Standard Deviation Function

def sd(x):	# x -> list
	if(len(x)!=0):
	
		meanx = sum(x)/len(x)	# Mean of the list.
		cumsum=0				# Cummulative Sum.
	
		for i in x:
			cumsum += (i-meanx)**2	# Variance.
	
		cumsum /= len(x)
		
		return (cumsum**0.5)	# Square root of variance.
	
	return 0	# No sd if there are no observations

# Function for Mean

def mean(x):
	return sum(x)/len(x)