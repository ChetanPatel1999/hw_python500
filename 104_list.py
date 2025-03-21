l1 = []
size = int(input("enter the size of list: "))

for i in range(size):
    typ= int(input("Enter element type: \n1.String\n2.Integer\n3.float\n4.List\n5.Tuple\n"))
    match typ:
     case 1:
        val = input(f"enter element {i+1}: ")
        l1.append(val)
        
     case 2:
        val2 = int(input(f"enter element {i+1}: "))
        l1.append(val2)
    
     case 3:
        val3 =float(input(f"enter element {i+1}: "))
        l1.append(val3)
        
     case 4:
        lisiz=int(input("Enter size of list: "))
        l2 = []
        for j in range(lisiz):
            val4 = input(f"enter element [{i+1}][{j+1}]: ")
            l2.append(val4)
            
        l1.append(l2)
     case 5:
        lisiz1=int(input("Enter size of list: "))
        l3 = []
        for k in range(lisiz1):
            val5 = input(f"enter element [{i+1}][{k+1}]: ")
            l3.append(val5)
        l3 = tuple(l3)
        l1.append(l3)
        
print(l1)