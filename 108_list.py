#wap to remove duplicate element in list.
l1=[12,34,5,6,5,12,5,34,12] # 4
l2=[]
for i in range(len(l1)):#i=1
    for j in range(i+1,len(l1)):#j=2
        if l1[i]==l1[j]:
            break
    else:
        l2.append(l1[i])    

print(l1)  
print(l2)  