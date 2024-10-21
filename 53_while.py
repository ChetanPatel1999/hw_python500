#wap to print sum 1 to 10.
# 1+2+3+4+5.....= 55
i=1
sum=0
while i<=10:
    if i<10:
         print(i,end=" + ") 
    else:
         print(i,end="")     
    sum+=i
    i+=1
print(f" = {sum}")    