#wap to print even number series in given range.
s=int(input("enter starting range : "))
e=int(input("enter ending range : "))
i=s
print(f"even number from {s} to {e} : ",end=" ")
while i<=e:
    if i%2==0:
        print(i,end=' ')
    i+=1