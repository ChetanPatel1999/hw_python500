#wap to shift all even number in left side in list.
l1=[77,99,67,8,9,44,68,7,33]
index=0
for i in range(len(l1)):
    if l1[i]%2==0:
        temp=l1[index]
        l1[index]=l1[i]
        l1[i]=temp
        index+=1
print(l1)        
