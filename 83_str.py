#wap to convert given string in upper case.
s=input("enter a string :")
print("string : ",s)#chetan
up=""
for i in s:
    if i>='a' and i<='z':
        up=up+chr(ord(i)-32)
    else:
        up=up+i    
print("upper case : ",up)

