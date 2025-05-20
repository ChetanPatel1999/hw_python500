#class and instance variable
class emp:
    count=0
    c_name="apple"
    def __init__(self,id,sal):
        self.id=id
        self.sal=sal
        emp.count+=1
    def display(self):
        print(f"emp info :")    
        print(f"emp company name : {emp.c_name}")    
        print(f"emp id : {self.id}")    
        print(f"emp sal : {self.sal}")    
    def emp_count():
        print("----------------------------")
        print(f"emp count : {emp.count}")        

e1=emp(101,12000)
e2=emp(102,45000)
e3=emp(103,15000)
e1.display()
e2.display()
e3.display()
emp.emp_count()