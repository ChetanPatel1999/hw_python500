#display data using fstring formate specifire
"""
%d for integer
%f for float
%c for character
%s for string
"""
a=12
b=56.78
c="chetan"
d="P"
ans=a+b
print("integer value of a = %d"%a)
print("float value of b = %.2f"%b)
print("string value of c = %s"%c)
print("charcter value  of d = %c"%d)
print("all valeus : %d %.2f %s %c"%(a,b,c,d))
print("sum of %d and %.2f = %.2f"%(a,b,ans))
