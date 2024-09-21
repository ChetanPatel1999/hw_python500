#display data using format method
a=12
b=56.78
c="chetan"
d="P"
ans=a+b
print("integer value of a = {}".format(a))
print("float value of b = {}".format(b))
print("string value of c = {}".format(c))
print("charcter value  of d = {}".format(d))
print("all valeus : {} {} {} {}".format(a,b,c,d))
print("sum of {} and {} = {}".format(a,b,ans))
print("sum of {2} and {0} = {1}".format(a,b,ans))
print("sum of {x} and {y} = {z}".format(x=a,y=b,z=ans))
