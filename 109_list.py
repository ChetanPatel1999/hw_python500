#wap to make new list only with uniqe element.
l1=[12,34,56,5,6,5,12,5,34,12] # 4
l2=[]
for i in range(len(l1)):#i=1
    c=0
    for j in range(len(l1)):#j=2
        if l1[i]==l1[j]:
           c+=1        
    if c==1:
        l2.append(l1[i])    
print(l1)  
print(l2)  