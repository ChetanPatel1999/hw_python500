#return more than one value
def cube_square(num):
    return (num*num),(num*num*num)


res=cube_square(4)
print(type(res))
print("square : ",res[0])
print("cube : ",res[1])
