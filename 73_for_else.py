#use of for else
num=int(input("enter a table : "))# 6
search=int(input("enter a num: "))# 76
for i in range(1,11):
    if search== num*i:
       print("num is found")
       break
else:
    print("num is not found")    
     