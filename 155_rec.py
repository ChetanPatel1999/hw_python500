#wap to print a msg 10 times using recursion.
def number(i):
    if i>1:
        number(i-1)
    print(i)    

#main program
number(5)
