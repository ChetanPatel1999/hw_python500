#class and object concept in python
class emp:
    def __init__(self,a,b):
        self.id=a
        self.sal=b
    def display(self):
        print("id : ",self.id)    
        print("sal : ",self.sal)  


e1=emp(101,1200.50)  
e2=emp() 
e1.display()       