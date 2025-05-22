class Student:
    def setdata(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per
    def display(self):
        print("student info : ")
        print(f"name of student : {self.name}")
        print(f"rno of student : {self.rno}")
        print(f"per of student : {self.per}")

class MathStudent(Student):
    def setMarks(self,s1,s2,s3):
        self.math=s1
        self.physic=s2
        self.chemestry=s3
    def displayMarks(self):
        print("student marks : ")    
        print(f"Math marks :{self.math} ")    
        print(f"physic marks :{self.physic} ")    
        print(f"chemestry marks :{self.chemestry} ") 

class CommersStudent(Student):
    def setMarks(self,s1,s2,s3):
        self.account=s1
        self.ip=s2
        self.business=s3
    def displayMarks(self):
        print("student marks : ")    
        print(f"account marks :{self.account} ")    
        print(f"ip marks :{self.ip} ")    
        print(f"business marks :{self.business} ") 

s1=MathStudent()
s1.setdata("ram",101,89)
s1.setMarks(56,78,90)
s1.display()
s1.displayMarks()
print("------------------------")
s2=CommersStudent()
s2.setdata("shyam",102,55)
s2.setMarks(44,54,66)
s2.display()
s2.displayMarks()