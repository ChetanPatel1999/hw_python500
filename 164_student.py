class Student:
    def setStudent(self,name,rno,per):
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

s1=Student()
s1.setStudent("ram",101,78)
s2=Student()
s2.setStudent("shyam",102,23)
s3=Student()
s3.setStudent("hariom",103,50)
s1.displayResult()
s2.displayResult()
s3.displayResult()