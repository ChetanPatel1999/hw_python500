class Student:
    def __init__(self,name,rno,per):  # constructor
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
       

s1=Student("ram",101,78)
s2=Student("shyam",102,23)
s3=Student("hariom",103,50)
s1.displayResult()
s2.displayResult()
s3.displayResult()