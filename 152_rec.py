#wap to print 1 to 20 even number using recursion 
i=1
def fun():
    global i
    if i%2==0:
         print(i,end=" ")
    i=i+1
    if i<=20:
        fun()


#call in main program
fun()