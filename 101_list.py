#wap to make a new list with square element of previus list.
#newlist = [expression for item in iterable if condition == True] 
l1=[3,2,7,4,8]
l2=[i*i for i in l1 if i%2==0]
print(l1)
print(l2)

l3=[2,5,8,9]
l4=[]
for i in l3:
    if i%2==0:
        s=i*i
        l4.append(s)
print(l3)
print(l4)        
