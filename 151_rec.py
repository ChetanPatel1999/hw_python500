#wap to print 1 to 10 number using recursion 
i=1
def fun():
    global i
    print(i,end=" ")
    i=i+1
    if i<=10:
        fun()


#call in main program
fun()