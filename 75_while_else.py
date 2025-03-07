#wap to check 3 is in given number or not.
num=int(input("enter a num : "))#24
while num:
    rem=num%10
    if rem==3:
        print("3 is found ")
        break
    num=num//10 
else:
    print("3 is not found")          

