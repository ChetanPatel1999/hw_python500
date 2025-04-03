# copy() method is used to make copy of dictionary
# dict1 = { 
# "brand": "Ford", 
# "model": "Mustang", 
# "year": 1964 
# }
# dict2=dict1
# dict2
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# dict2['brand']="thar"
# dict2
# {'brand': 'thar', 'model': 'Mustang', 'year': 1964}
# dict1
# {'brand': 'thar', 'model': 'Mustang', 'year': 1964}
# dict2=dict1.copy()
# dict2
# {'brand': 'thar', 'model': 'Mustang', 'year': 1964}
# dict1
# {'brand': 'thar', 'model': 'Mustang', 'year': 1964}
# dict2['year']=2000
# dict2
# {'brand': 'thar', 'model': 'Mustang', 'year': 2000}
# dict1
# {'brand': 'thar', 'model': 'Mustang', 'year': 1964}
dict1 = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
mydict = dict(dict1) 
print(mydict)
mydict['brand']="thar" 
print(mydict)
print(dict1)

