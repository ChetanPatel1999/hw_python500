#wap to print table of given number using recursion 
i=1
def table(n):
    global i
    print(f"{n} x {i} = {n*i}")
    i=i+1
    if i<=10:
        table(n)


#call in main program
table(11)