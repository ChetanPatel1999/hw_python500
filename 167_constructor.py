#Constructor with Default Values 
class Student:
    def __init__(self,name,rno,per=40): 
        self.name=name
        self.rno=rno
        self.per=per
    def displayResult(self):
        print("Student Result ..... ")
        print(f"Student Name : {self.name}")    
        print(f"Student Rno : {self.rno}")    
        print(f"Student Percentage : {self.per}")
        if self.per>33:
            print("Student Pass")
        else:
            print("Student Fail") 
        print("------------------------------") 
       

s1=Student("ram1",101)
s2=Student("ram2",102,45)
s3=Student("ram3",103,77)
s1.displayResult()
s2.displayResult()
s3.displayResult()