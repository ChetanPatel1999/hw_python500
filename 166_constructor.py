class Student:
    def __init__(self):  #non - parameterized constructor
        self.name="chetan"
        self.rno=101
        self.per=78.90
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
s2=Student()
s3=Student()
s1.displayResult()
s2.displayResult()
s3.displayResult()