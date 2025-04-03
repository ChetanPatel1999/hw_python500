# Nested Dictionaries
#  A dictionary can contain dictionaries, this is called nested dictionaries. 
# Example : Create a dictionary that contain three dictionaries: 

myfamily = { 
"child1" : { 
"name" : "Emil", 
"year" : 2004 
}, 
"child2" : { 
"name" : "Tobias", 
"year" : 2007 
}, 
"child3" : { 
"name" : "Linus", 
"year" : 2011 
} 
} 
print(myfamily)
print(myfamily["child2"]['name'])
del myfamily["child2"]['name']
print(myfamily)
myfamily["child2"]['name']="rambo"
print(myfamily)