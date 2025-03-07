#use of break stmnt
num=int(input("enter a table : "))# 6
search=int(input("enter a num: "))# 36
is_found=False
for i in range(1,11):
    if search== num*i:
        is_found=True
        break
if is_found:
    print("num is found")    
else :
    print("num is not found")      