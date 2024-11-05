#wap to check given number is prime or not.
num=int(input("enter a num : "))#15
isprime=True
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if isprime:
    print("num is prime")  
else:
    print("num is not prime")          

