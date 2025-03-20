#The extend() method does not have to append lists, you can add any iterable 
#object (tuples, sets, dictionaries etc.).
list1 = ["apple", "banana", "cherry"] 
tropical = ["mango", "pineapple", "papaya"] 
list1.extend(tropical) 
list2=[12,34,56]
list1=list1+list2
list1.extend("hello")
list1.extend({12:456,13:567})
print(list1) 