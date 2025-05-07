class dog:
    def setDog(self):
        self.name=input("enter dog name: ")
        self.color=input("enter dog color: ")
        self.age=int(input("enter dog color: "))

    def displayDog(self):
        print("dog info :")
        print(f"dog name : {self.name}")
        print(f"dog color : {self.color}")
        print(f"dog age : {self.age}")
    

d1=dog()
d1.setDog()
d2=dog()
d2.setDog()
d1.displayDog()
d2.displayDog()
    


