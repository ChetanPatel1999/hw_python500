#wap to print sum 1 to 10 number using recursion.
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)   

print(f"sum 1 to 10 : {sum(10)}") 
print(f"sum 1 to 11 : {sum(11)}") 