dict1 = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
print(dict1.pop("model"))
print(dict1)
print(dict1.popitem())
print(dict1)

del dict1['brand']
print(dict1)

dict2={'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(dict2)
dict2.clear()
print(dict2)