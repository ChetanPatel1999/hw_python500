#Looping Using List Comprehension
#wap to make a list of even value.
l1=[12,34,5,78,9]
l2=[]
l3=[]
for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)    
print(l1)        
print(l2)  
print(l3)  

l1=[12,34,5,78,9]
l2=[i for i in l1 if i%2==0]  
l3=[i for i in l1 if i%2==1]  
print(l2)   
print(l3)   


