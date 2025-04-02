#dict  keys() , values() , items() , get() method
dict1 = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)  

for i in dict1.items():
    print(i)

for i in dict1:
    print(dict1.get(i))

for i in dict1:
    print(dict1[i])


for i in dict1:
    print(i)    