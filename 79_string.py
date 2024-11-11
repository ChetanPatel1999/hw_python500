#wap to take a string form user and print string like.
#input =>  hello
# output => h+e+l+l+o
s=input("enter a string :") # ujjain
l=len(s)
for i in s: #hello
    if i != s[l-1]:
        print(i,end="+")
    else:
        print(i)    

