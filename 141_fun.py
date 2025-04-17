# Function Arguments 
# You can call a function by using the following types of formal arguments − 
#  Required arguments 
#  Keyword arguments 
#  Default arguments 
#  Variable-length arguments
def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True    
print(prime(18,9))