#wap to check greatest number between three number without using logical and opeartor.
num1=int(input("enter a num1 : "))#56
num2=int(input("enter a num2 : "))#88
num3=int(input("enter a num3 : "))#889
if num1>num2:
    if num1>num3:
        print("gratest num = ",num1)
    else:
        print("gratest num = ",num3)    
else :
    if num2>num3:
        print("gratest num = ",num2) 
    else:
        print("gratest num = ",num3)      