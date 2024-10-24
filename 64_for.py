#wap to print even number in given range.
s=int(input("enter starting range : "))#11
e=int(input("enter ending range : "))#20
print("even number serise : ",end="")
for i in range(s,e): # 12
     if i%2==0:
        print(i,end=" ")