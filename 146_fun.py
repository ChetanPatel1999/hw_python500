#Pass by Reference or pass by value
def fun(a):
    print(a)#34
    a=56
def fun2(l):
    print("l[1] : ",l[1])
    l[1]=777
b=34
#call by value
fun(b)
print(b) #34 

l1=[12,34,56,78,90]
#call by reference
fun2(l1)
print("l1[1] : ",l1[1])