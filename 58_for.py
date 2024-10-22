#wap to print only vovel in given string.
s=input("enter a string : ") # chetan
print(f"string : {s}")
print("vovels in string : ",end="")
for ch in s:
    if ch in 'aieou':
        print(ch,end="")
