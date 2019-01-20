# ------------------------------------
#	PROGRAM FOR MULTIPLE REGRESSION
# ------------------------------------

# File Imports

from sigma import *

# Execution

try:
	n = int(input("\n\nEnter the number of observations : "))
except ValueError:
	print("\n\nYou entered the wrong input. Restart the program.\n\n")
	exit()	# Kill The Kernel and the process.

n = abs(n)	# Convert n to positive number if negative is entered.

if(n==0):
	exit()	# End the program right now if the number of obs is 0.

inputlist = [[],[],[]]	# List of Observations

# Accepting input

for i in range(0,3):
	char = 'X1' if i==0 else 'X2' if i==1 else 'X3'
	print("\nEnter the values for %s" %(char))
	
	for j in range(0,n):
		try:
			inputlist[i].append(float(input("\nValue %d : " %(j+1))))
		except:
			print("\n\nSomething went wrong.\n\n")	# Might be any error.
			exit()	# Kill the kernel and the process.

# Accepting of Values done. Now Stuff Of Regression Begins.

# Correlation Coefficients

r12 = corr(inputlist[0],inputlist[1])
r13 = corr(inputlist[0],inputlist[2])
r23 = corr(inputlist[1],inputlist[2])

# Cofactors

R11 = (1 - (r23**2))
R22 = (1 - (r13**2))
R33 = (1 - (r12**2))
R31 = (r12*r23 - r13)
R32 = (r12*r13 - r23)

# Partial Regression Coefficients - Yule's Notations

b31_2 = float((-sd(inputlist[2]))/(sd(inputlist[0])))*(float(R31/R33))	# Partial Regression Coefficient of X1 on X3. Excluding the effect of X2.
b32_1 = float((-sd(inputlist[2]))/(sd(inputlist[1])))*(float(R32/R33))	# Partial Regression Coefficient of X2 on X3. Excluding the effect of X1.

# Constant a = mean(X3) - b31.2 * mean(X1) - b32.1 * mean(X2)

a = float(mean(inputlist[2]) - b31_2*mean(inputlist[0]) - b32_1*mean(inputlist[1]))

# Asking the user to input the values for which the value has to be estimated.

try:
	finalx1 = float(input("\nEnter the value of X1 to estimate X3 : "))
	finalx2 = float(input("\nEnter the value of X2 to estimate X3 : "))
except ValueError:
	exit()	# Kill the process.

# Calculating the value of X3 : 

# By the method of Least Squares : X3 = a + b31.2 * X1 + b32.1 * X2

finalx3 = float(a + b31_2*finalx1 + b32_1*finalx2);

print("\n\nThe Estimated Value of X3 is : %f" %(finalx3));