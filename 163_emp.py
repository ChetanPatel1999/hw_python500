class emp:
    def setEmp(self):
        self.id=int(input("enter id : "))
        self.sallary=eval(input("enter sallary : "))
    def dispEmp(self):
        print("emp info : ")
        print(f"emp id : {self.id}")    
        print(f"emp sallary : {self.sallary}")    
        print("-----------------------")    

#create employ
employs=[]
n=int(input("enter num of emp : "))
for i in range(n):
    e=emp()
    e.setEmp()
    employs.append(e)  

# for i in range(n):
#    employs[i].dispEmp()

for i in employs:
   i.dispEmp()

#disply only sallary 5000 above
print("above 5000 sallary emp : ")
for i in employs:
   if i.sallary>5000:
       i.dispEmp()  

