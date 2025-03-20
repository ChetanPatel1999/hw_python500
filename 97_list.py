list1 = ["apple", "banana", "cherry"] 
del list1[0] 
print(list1) 
l1=[12,34,56,67,89,90]
del l1[2:6:2]
print(l1)
l1=[12,33,45,[1,2,3,4]]
del l1[3][1]
print(l1)
#Clear the List 
# The clear() method empties the list. 
# The list still remains, but it has no content.
list1 = ["apple", "banana", "cherry"] 
list1.clear() 
print(list1) 