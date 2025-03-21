#wap to count duplicate elemet in list.
l1=[12,34,5,6,5,12,5,34,12] # 4
c=0
for i in range(len(l1)):#i=1
    for j in range(i+1,len(l1)):#j=2
        if l1[i]==l1[j]:
            c+=1
            break
print(f"count = {c}")            


