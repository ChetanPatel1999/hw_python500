#wap to count word in given string
s=input("enter a string :")
print("string : ",s)#   hi       
cn=1
j=False
for i in range(len(s)):
    if s[i]!=' ':
        j=True
    if j==True and i!=len(s)-1 and ord(s[i])==32 and ord(s[i+1])!=32:
        cn+=1   
print("total word : ",cn)        

