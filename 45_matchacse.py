#simple calulater project
num=int(input("""wlelcome to my calculater ...
press 1 for add
press 2 for sub
press 3 for mul
press 4 for div
press num : """))
match num:
    case 1:
        a=eval(input("enter frist num : "))
        b=eval(input("enter second num : "))
        c=a+b
        print("sum = ",c)
    case 2:
        a=eval(input("enter frist num : "))
        b=eval(input("enter second num : "))
        c=a-b
        print("sub = ",c) 
    case _:
        print("please press 1 to 4")       
