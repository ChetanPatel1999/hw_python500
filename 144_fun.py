#Variable-length arguments
#  We can use special characters in Python functions to pass as many arguments as 
# we want in a function. There are two types of characters that we can use for this 
# purpose: 
# 1. *args -These are Non-Keyword Arguments 
# 2. **kwargs - These are Keyword Arguments. 


# *args -These are Non-Keyword Arguments 
def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    print("add : ",sum)

def student(*name,marks):
    print("student name : ",name)
    print("student marks : ",marks)

#**kwargs - These are Keyword Arguments.
def shop(**item):
    print("item : ",item)

#function call
shop(pen=10,book=50,pencil=5)
add(12)
add(12,7)  
add(4,5,7)
add(34,5,1,10,30)
student("ram",78,marks=45)
student("ram",78,45,marks=90)