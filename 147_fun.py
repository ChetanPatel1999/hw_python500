#pass by reference
def fun(d):
    d["name"]="chetan"


#function call
d1={"name":"ram","age":12}
fun(d1)
print(d1)