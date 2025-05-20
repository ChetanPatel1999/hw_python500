class student:
    totalpass=0
    totalfail=0
    totalstd=0
    def __init__(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per
        student.totalstd+=1
    def result_display(self):
        print("student result......")
        print(f"student name : {self.name}")
        print(f"student rno : {self.rno}")
        print(f"student per : {self.per}")
        if self.per>33:
            print("student pass")
            student.totalpass+=1
        else:
            print("student Fail")
            student.totalfail+=1 
        print("-----------------------------------")       
    def total_result():
        print(f"total pass : {student.totalpass}")
        print(f"total fail : {student.totalfail}")
        print("-----------------------------------") 
    def totalstudent():
        print(f"total student : {student.totalstd}")
        print("-----------------------------------") 

s1=student("ram",101,20)
s2=student("shyam",102,70)
s3=student("hariom",103,30)
s1.result_display()
s2.result_display()
s3.result_display()
student.total_result()
student.totalstudent()