#  Unpacking a Tuple
#  When we create a tuple, we normally assign values to it. This is called 
# "packing" a tuple.
# But, in Python, we are also allowed to extract the values back into variables. 
# This is called "unpacking": 
t1=(12,34,56)
a,b,c=t1
print(a,b,c)
a,*b=t1
print(a,b)

# we can use * operator to repeat tuple
t1=(12,34,12,56)
t2=t1*3
print(t2)

print(t1.count(12))
print(t1.index(34))
