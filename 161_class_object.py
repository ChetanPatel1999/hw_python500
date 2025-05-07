class dog:
    def setDog(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age

    def displayDog(self):
        print("dog info :")
        print(f"dog name : {self.name}")
        print(f"dog color : {self.color}")
        print(f"dog age : {self.age}")

d1=dog()
d1.setDog("tomy","red",12)
d2=dog()
d2.setDog("wifi","white",8)
d1.displayDog()
d2.displayDog()
    


