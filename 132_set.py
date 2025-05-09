# You can use the union () method that returns a new set containing all items from 
# both sets, and the update () method that inserts all the items from one set into 
# another: 
# Example: The union() method returns a new set with all items from both sets: 
set1 = {"a", "b", "c"} 
set2 = {1, 2, 3,'a'} 
# set3 = set1.union(set2) 
set3=set1|set2
print(set3) 
# Example: The update() method inserts the items in set2 into set1: 
set1 = {"a", "b" , "c"} 
set2 = {1, 2, 3,'a'} 
set1.update(set2) 
print(set1)