#we can also return multiple value
def alloperation(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    l2=[1,2,3,4]
    return add,sub,mul,div,"home",[12,34,56],l2
t1=alloperation(12,5)
print(type(t1))
print(t1)