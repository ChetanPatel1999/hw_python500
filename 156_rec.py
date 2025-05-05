#wap to find factorial of given number using recursion
def factorial(n):
    if n==0 :
        return 1 
    return n*factorial(n-1)

print(f"factorial of 5 = {factorial(5)}")
print(f"factorial of 6 = {factorial(6)}")