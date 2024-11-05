#wap to check given number is prime or not.
num=int(input("enter a num : "))#15
for i in range(2,num):
    if num%i==0:
        print("num is not prime") 
        break   
else:
    print("num is prime")          

