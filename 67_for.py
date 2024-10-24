#wap to print factors of given number.
#12 =  1 2 3 4 6 12
#20 = 1 2 4 5 10 20
num= int(input("enter a num : "))#15
for i in range(1,num+1):# i=6
    if num%i==0:
        print(i,end=" ")# 1 3 5 15