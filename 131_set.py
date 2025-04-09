#remove method
# Note: If the item to remove does not exist, remove () will raise an error. 
set1 = {"apple", "banana", "cherry"} 
set1.remove("banana") 
print(set1) 
#discard method
# Note: If the item to discard does not exist, discard () will not raise an error. 
set1 = {"apple", "banana", "cherry"} 
set1.discard("banan") 
print(set1) 
#pop  method
set1 = {"apple", "banana", "cherry"} 
x = set1.pop() 
print(x) 
print(set1)
#clear method
set1.clear()
print(set1)
#del keyword
del set1
print(set1)
