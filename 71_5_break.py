#wap to check given number is prime or not.
num=int(input("enter a num : "))#400
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
        if count==3:
            break
if count==2:
    print("prime") 
else:
    print("not prime")           


