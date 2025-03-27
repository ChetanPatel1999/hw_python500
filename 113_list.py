# selection sort
l1=[5,213,6,3,34,43,7]
#[3,5,6,213,34,43,7]   
for i in range(len(l1)):#2
    min=l1[i]#6
    index=i # 1
    for j in range(i+1,len(l1)):#2 < 7
        if l1[j] < min :
            min=l1[j]  #5
            index=j # 3
    temp=l1[i] # 213
    l1[i]=min
    l1[index]=temp  
print(l1)          