#mini clube managamnet project
age=int(input("enter your age : "))
if age>=18:
    print("welcome to my clube ...")
    print("1. pasta    : 120")
    print("2.sandwitch : 150")
    print("3.noodles   : 90")
    num=int(input("please order to press num : "))
    if num==1:
        print("your pasta order is done please pay 120")    
    elif num==2:
        print("your sandwitch order is done please pay 150")
    elif num==3:
        print("your noodles order is done please pay 90")  
    else:
        print("choose correct opetion...")            
else:
    print(f"you are under age try after {18-age} year")    