#print state name acording to state short form.
state=input("enter short state name : ")#op
match state:
    case "mp" :
        print("madhya pradesh")
    case "rj" :
        print("rajesthan")
    case "up":
        print("utter pradesh")    
    case _ :
        print("please enter valid short name")    
