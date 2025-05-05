#wap to print a msg 5 times using recursion 
i=1
def fun():
    global i
    print("hello student")
    i=i+1
    if i<=5:
        fun()


#call in main program
fun()