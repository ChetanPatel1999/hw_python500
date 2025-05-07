class dog:
    def setDog(s,n,c,a):
        s.name=n
        s.color=c
        s.age=a

    def displayDog(y):
        print("dog info :")
        print(f"dog name : {y.name}")
        print(f"dog color : {y.color}")
        print(f"dog age : {y.age}")

d1=dog()
d1.setDog("tomy","red",12)
d2=dog()
d2.setDog("wifi","white",8)
d1.displayDog()
d2.displayDog()
    


