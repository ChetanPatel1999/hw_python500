#wap to find a element in list using liner searching.
l1=[45,67,89,23,44]
el=int(input("enter a element : "))
for i in l1:
    if i==el:
        print("element found")
        break
else:
    print("element not found")    