# super() is used to point parant class data.
class Bowler:
    def setBowler(self,Tover,Tmatch):
        self.Tover=Tover
        self.Tmatch=Tmatch
    def getBowler(self):
        print("bowler info : ")
        print(f"total over : {self.Tover}")    
        print(f"total match : {self.Tmatch}")  
class BestMan:
    def setBestMan(self,runRate,Tsix):
        self.runRate=runRate
        self.Tsix=Tsix
    def getBestMan(self):
        print("BestMan info : ")
        print(f"total runRate : {self.runRate}")    
        print(f"total six : {self.Tsix}")      

class AllRounder(Bowler,BestMan):
    def setAllRounder(self,a,b,c,d):
        super().setBowler(a,b)
        super().setBestMan(c,d)         
    def getAllRounder(self):
        super().getBowler()
        super().getBestMan()
p1=AllRounder()
p1.setAllRounder(100,2,78.4,12)
p1.getAllRounder()
