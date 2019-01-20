# -------------------- -----------------------------
# Program to estimate values of Y based on X.
# -------------------- -----------------------------

#---------------- -------------------
# Functions required for the program 
# --------------- -------------------


# Function to accept the list of numbers towards the number of elements provided by the user.

def accept(X,Y,n):
    print("\n\nInputs : \n")
    
    for i in range(0,n):
        try:
            m=float(input("\nElement "+str(i+1)+" : "))
        except ValueError:
            print("\nInvalid Values Entered.\nKilling Process.\n")
            exit()          # Killing the Kernel.
        X.append(m)
    
    print("\n\nOutputs : \n")
    
    for i in range(0,n):
        try:
            m=float(input("\nElement "+str(i+1)+" : "))
        except ValueError:
            print("\nInvalid Values Entered.\nKilling Process.\n")
            exit()          # Killing the Kernel.
        Y.append(m)

# Function to find the co-variance of the two variables

def cov(X,Y,n):
    xmean=(sum(X)/n)        # Mean of Inputs
    ymean=(sum(Y)/n)        # Mean of Outputs
    
    product=0        # Variable to store the product of respective values of X and Y.
    cv=1            # Variable to store the covariance of X and Y. 
    
    for i in range(0,n):
        product=product+(X[i]*Y[i])
    
    cv=((product/n) - (xmean*ymean))
    
    return cv

# Function to estimate the value at X=Whatever input the user gave.

def est(cv,X,Y,x,n):
    xmean=sum(X)/n
    ymean=sum(Y)/n
    
    sumx2=0       # Variable to find the product of all the squares of the numbers in the input list.
    
    # Variables for regression line :
    
    a=1
    b=1
    
    for i in range(0,n):
        sumx2=sumx2+(X[i]**2)
        i=i+1
    
    varx=((sumx2/n)-(xmean**2))        # Variance of x
    
    if(varx!=0):
        b=cv/varx                          # Slope in the regression line of Y on X.
        a=(ymean-(b*xmean))                # Constant in the regression line of Y on X.
    
    return (a+b*x)           # Final    


# Lists of numbers

X=[]
Y=[]

# Total Number of Observations

try:
    n=int(input("\nEnter the total no of observations : "))
except ValueError:
    print("\n\nInvalid Value Entered.\n Killing Process.\n")
    exit()

n=abs(n)      # Converted value of n to positive if it was negative.
count=0       # Variable to count the number of occurences of a single element.

if(n!=0):
    accept(X,Y,n)
    cv=cov(X,Y,n)
    
    for i in X:
        for j in X:
            if(i==j):
                count=count+1
    
    if(count!=n**2):       # If all the elements in the inputs are the same, then there will be a divide by 0 error.
        try:
            x=float(input("\n\nEnter the value to estimate at : "))
        except ValueError:
            exit()

        final=est(cv,X,Y,x,n)   # Final Estimation
        print("\n\nThe estimated value is : "+str(final))
    else:
        print("\n\nVariance of the set of inputs is 0. Hence, estimation cannot be performed.")
else:
    print("\n\nThe number of inputs cannot be negative.")