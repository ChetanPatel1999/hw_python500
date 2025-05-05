#make a function find power of given number using recursion.
# def pow(n,p):
#     ans=1
#     for i in range(p):
#         ans=ans*n
#     return ans    
def pow(n,p):
    if p==0:
        return 1
    return n*pow(n,p-1)
# function call
print(f"power : {pow(5,3)}")
print(f"power : {pow(5,2)}")
print(f"power : {pow(2,4)}")
print(f"power : {pow(4,4)}")