from standard import sd, mean
from covariance import cov

# Program to find out the correlation between two variables.

def corr(x,y):		# x and y are datasets of two variables.
	return (cov(x,y)/(sd(x)*sd(y)))	# Correlation Co-efficient between two variables.