#wap to remove duplicate elemet in list.
l1=[12,34,5,6,5,12,5,34,12] # 4
l2=[]
for i in l1:#i=12
    if i not in l2:
        l2.append(i)
print(l1)        
print(l2)            
