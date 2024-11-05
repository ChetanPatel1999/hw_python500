#use of break stmnt
num=int(input("enter a table : "))# 6
search=int(input("enter a num: "))# 76
found=False
for i in range(1,11):
    if search== num*i:
        found=True
        break
if found:
    print("num is found")    
else :
    print("num is not found")      