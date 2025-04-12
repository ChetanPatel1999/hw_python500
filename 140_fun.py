def graetest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
def graet(a,b,c):
    return a if a>b and a>c else b if b>c else c   
print(graetest(12,34,56))
print(graetest(12,56,34))
print(graetest(56,5,34))
print(graet(56,5,34))
print(graet(56,5,34))