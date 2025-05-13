#constructor overloding not posible in python
class demo:
    def __init__(self):
        print("0 arg constructor is called")
    def __init__(self,a,b):
        print("2 arg constructor is called")  
    def __init__(self,a,b,c):
        print("3 arg constructor is called")       

d1=demo(12,78,88)