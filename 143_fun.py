#Default arguments 
def add(a=5,b=7,c=90):  # 90 is default value
    print("sum = ",(a+b+c))

def bill(quantity,price=100):
    print("bill : ",(quantity*price))

#function call
add(12,7,8) 
add(12,20) 
add(9)  
add()
bill(5,400)
bill(10)
bill(quantity=7,price=90)