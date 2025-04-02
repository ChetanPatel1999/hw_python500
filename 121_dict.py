#how to take dictionary from user
marks={}
n=int(input("enter a dict size : "))
for i in range(n):
    key=input("enter subject name : ")
    value=int(input("enter marks : "))
    #marks[key]=value
    marks.update({key:value})
print(marks)    