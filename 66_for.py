#wap to print sum of all even number in given range.
s=int(input("enter starting range : "))#1
e=int(input("enter ending range : "))#11
sum=0
for i in range(s,e): # 12
     if i%2==0:
        sum=sum+i
print("sum of all even number is : ",sum)        